import os
from ConvexHull import *
import matplotlib.pyplot as plt
from Grow_Obstacle import *

#**Global Var Definition
start = []
goal = []
world = []
obs = []
initial_obs = []
convex_obs = []


#***********************************************
configurefile = open("configure.txt",'r')

cnt = 0
obs_cnt = 0
obpts = 0
read_obs_pts = False
while True:
    line = configurefile.readline()
    paras = line.split(' ')
   # print len(paras)
    if cnt == 0:
        start = [float(paras[0]),float(paras[1].split('\n')[0])]
        print start
    if cnt == 1:
        goal = [float(paras[0]),float(paras[1].split('\n')[0])]
        print goal
    if cnt == 2:
        world = [float(paras[0]),float(paras[1].split('\n')[0])]
    if cnt == 3:
        #print paras[0].split('\n')[0]
        obs_cnt = paras[0].split('\n')[0]
        #print obs_cnt
        break
    cnt += 1

for i in range(0,int(obs_cnt)):
    fline = configurefile.readline()
    #print fline
    fparas = fline.split(' ')
    obpts = int(fparas[0].split('\n')[0])
    while obpts >= 1:
        fline = configurefile.readline()
        fparas = fline.split(' ')
        #print fparas
        obs = obs + [(float(fparas[0]), float(fparas[1].split('\n')[0]))]
        obpts -= 1
    print i
    initial_obs.append(obs)
    obs = []
    print initial_obs
x = []
y = []
for ibos in initial_obs:
    for item in ibos:
        x.append(item[0])
        y.append(item[1])
x.append(start[0])
y.append(start[1])
x.append(goal[0])
y.append(goal[1])
plt.scatter(x,y)

initial_obs = my_grow_obs(start[0],start[1],0,initial_obs)
print initial_obs
x = []
y = []
for ibos in initial_obs:
    for item in ibos:
        x.append(item[0])
        y.append(item[1])
x.append(start[0])
y.append(start[1])
x.append(goal[0])
y.append(goal[1])
plt.scatter(x,y,color='red')

convex_obs = get_convex(initial_obs)
plt.show()