
from gopigo import *
import math
import numpy as np
import time
import matplotlib.pyplot as plt

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

plt.plot([row[0] for row in nexts],[row[1] for row in nexts])
plt.show()
#[CHECK]
def rotate_itselfR(target):
    print 'R'+str(target)
    if target == 0:
        return

def rotate_itselfL(target):
    print 'L'+str(target)
    if target == 0:
        return


def move_cart(distance,cnt):
    global dist_per_cnt
    move_enc_cnt = int(distance/dist_per_cnt)
    print 'move'+str(move_enc_cnt)


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
        rotate_itselfR(target)
    else:
        rotate_itselfL(target)
    move_cart(dist,cnt)

cnt = 0
while nexts:
    prev = nexts.pop()
    if len(nexts) == 0:
        stop()
        break
    next = nexts[len(nexts)-1]
    parse_command(prev,next,cnt)
    cnt += 1
print 'done'