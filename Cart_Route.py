
from gopigo import *
import math
import numpy as np
import time
import matplotlib.pyplot as plt
from cam_way_point import *

enable_encoders()
enable_servo()


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

    enc_tgt(1, 1, target)
    set_speed(120)
    right_rot()
    time.sleep(2)


def rotate_itselfL(target,cnt):
    print 'L'+str(target)
    print cnt
    if target == 0 and cnt != 7:
        return
    elif target == 2:
        target += 1
    elif target == 0 and cnt == 7:
        rotate_itselfL(3,7)
        rotate_itselfR(2,7)
        return
    print 'realt'+str(target)

    enc_tgt(1, 1, target)
    set_speed(120)
    left_rot()
    time.sleep(3)


def move_cart(distance,cnt):
    global dist_per_cnt
    move_enc_cnt = int(distance/dist_per_cnt)
    print 'dist'+str(distance)
    print 'move'+str(move_enc_cnt)

    enc_tgt(1,1,move_enc_cnt)
    set_speed(255)
    fwd()
    time.sleep(5)


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
    if dist < 5:
        if deg == 179:
            enc_tgt(1, 1, 3)
            set_speed(100)
            right_rot()
            time.sleep(1)
            enc_tgt(1, 1, 2)
            set_speed(120)
            fwd()
            time.sleep(2)
            enc_tgt(1, 1, 3)
            set_speed(100)
            left_rot()
            time.sleep(1)

us_test(179)
cnt = 0

flag = input('use cam? 1:yes 2:no')

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

if flag == 1:
    move_ok = cam_to_goal(flag)
    if move_ok == True:
        servo(90)
        while us_dist(15) > 10:
            enc_tgt(1, 1, 10)
            set_speed(180)
            fwd()
            time.sleep(2)
    else:
        print 'whaaaat?'
else:
    print 'really done'

print 'hope this is goal'