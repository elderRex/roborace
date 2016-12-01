
from gopigo import *
import math
import numpy as np
import time
import matplotlib.pyplot as plt
import psutil

'''
enable_encoders()
enable_servo()
'''

car_axis = 11.55
r = car_axis / 2
perimeter = 20.4
dist_per_cnt = 1.04

cur_ori = 90

nexts = []

with open('Route_For_race.txt','r') as routefile:
    for line in routefile:
        paras = line.split(',')
        nexts.append([float(paras[0]),float(paras[1])])
nexts.reverse()
#print nexts

#plt.plot([row[0] for row in nexts],[row[1] for row in nexts])
#plt.show()
#[CHECK]
def rotate_itselfR(target,cnt):
    print 'R'+str(target)
    if target == 0:
        return
    if target == 2:
        target += 0
    enc_tgt(1, 1, target)
    set_speed(180)
    right_rot()
    time.sleep(1)

def rotate_itselfL(target,cnt):
    print 'L'+str(target)

    if target == 0 and cnt != 7:
        target = 1
    elif target == 2:
        target += 1
    elif target == 0 and cnt == 7:
        target += 2
    enc_tgt(1, 1, target)
    set_speed(150)
    left_rot()
    time.sleep(1)

def move_cart(distance,cnt):
    global dist_per_cnt
    move_enc_cnt = int(distance/dist_per_cnt)
    print 'move'+str(move_enc_cnt)
    enc_tgt(1,1,move_enc_cnt)
    set_speed(255)
    fwd()
    time.sleep(3)
    '''
    if cnt == 0:
        time.sleep(3)
    if cnt == 3:
        time.sleep(2)
    if cnt == 4:
        time.sleep(2)
    if cnt == 5:
        time.sleep(2)
    if cnt == 7:
        time.sleep(2)
    else:
        time.sleep(1)
    '''

def parse_command(prev,next,cnt):
    global r
    global perimeter
    global cur_ori
    print '('+str(prev)+' to '+ str(next)+')'
    dist = math.sqrt(pow(prev[0]-next[0],2)+pow(prev[1]-next[1],2))
    cos = (next[0]-prev[0])/dist
    angle_move_rad = math.acos(cos)
    angle_move_degree = math.degrees(angle_move_rad)
    actual_turn = cur_ori - angle_move_degree
    print 'ori_at_prev'+str(cur_ori)
    cur_ori = cur_ori - actual_turn
    print 'ori after turn'+str(cur_ori)
    target = int((abs(actual_turn) * math.pi/ 180) * r * 18 / perimeter)
    print target
    print actual_turn
    if actual_turn > 0:
        rotate_itselfR(target,cnt)
    else:
        rotate_itselfL(target,cnt)
    move_cart(dist,cnt)

def us_test(deg):
    servo(deg)
    dist = us_dist(15)
    if dist < 10:
        stop()

us_test(179)
cnt = 0
while nexts:
    prev = nexts.pop()
    if len(nexts) == 0:
        stop()
        break
    next = nexts[len(nexts)-1]
    parse_command(prev,next,cnt)
    cnt += 1
us_test(90)
print 'done'