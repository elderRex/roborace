# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import numpy as np
import time
import cv2
import io
import math
from gopigo import *
import sys
import math

enable_encoders()

list_of_clicks = []
avg_threshhold = 0
record_flag = False

target_vec = []
mask = 0
low_thresh = []
high_thresh = []

target_center_old = []
target_center_new = []
dist_to_tar = 100
area_old = 0
area_new = 0
manual_lag_cnt = 4

# used for naive_movement
initial_area = 0

car_axis = 11.55
r = car_axis / 2
perimeter = 20.4

def cart_turn(dis, ori):
    target = 2
    print "target" + str(target)

    if ori == 'L':
        rotate_itselfL(abs(target))
    else:
        rotate_itselfR(abs(target))

def rotate_itselfR(target):
    enc_tgt(1, 1, target)
    set_speed(180)
    right_rot()

def rotate_itselfL(target):
    enc_tgt(1, 1, target)
    set_speed(180)
    left_rot()

def detect_blob(ori_img, thresh, ini):
    global target_center_new
    global target_center_old
    global area_new
    global area_old
    # Find the blob by finding the contours
    img, cnts, hierachy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    area = 0
    cX = 0
    cY = 0
    center = (-1, -1)
    large_contour = []
    # loop over the contours
    for c in cnts:
        # compute the center of each blob
        M = cv2.moments(c)
        # print(M["m00"])
        if (M['m00'] != 0):
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
        else:
            cX = 0
            cY = 0
        # Compute the area of each blob
        area_curr = cv2.contourArea(c)
        if area < area_curr:
            area = area_curr
            center = (cX, cY)
            large_contour = c

    cv2.drawContours(ori_img, large_contour, -1, (0, 255, 0), 3)
    cv2.circle(ori_img, center, 7, (0, 0, 255), -1)
    cv2.putText(ori_img, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # show the image
    return center


def get_mask(hsv, image, low, high):
    mask = cv2.inRange(hsv, low, high)
    mask = cv2.GaussianBlur(mask, (15, 15), 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
    eroded = cv2.erode(mask, kernel)
    mask = cv2.dilate(eroded, kernel)
    return mask

def cam_to_goal(record_flag):
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (480, 320)
    camera.framerate = 4
    rawCapture = PiRGBArray(camera, size=(480, 320))
    width = 320
    # allow the camera to warmup
    time.sleep(0.1)
    status = False
    i = 0
    while status == False:

        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.namedWindow('image')
        i = i + 1
        # if check_center == 0 it means its time to check for centroid again

        x = [178.0, 190.0, 241.0]
        y = [179.0, 208.0, 255.0]
        low_thresh = np.array(x, np.uint8)
        high_thresh = np.array(y, np.uint8)
        mask = get_mask(hsv, image, low_thresh, high_thresh)
        res = cv2.bitwise_and(image, image, mask=mask)
        center = detect_blob(image, mask, 1)
        cv2.imshow('image', res)
        print center[0]

        if center[0] == -1:
            print 'where is the target?'
            cart_turn(width / 2 - center[0], 'R')
        elif center[0] > width/2:
            cart_turn(center[0]-width/2,'L')
        elif center[0] < width/2:
            cart_turn(width/2-center[0],'R')
        else:
            status = True
        if center[0] < width/2 + 30 and center[0] > width/2 - 30:
            status = True

        rawCapture.truncate(0)

    return True