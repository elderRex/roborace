import os
from ConvexHull import *
import matplotlib.pyplot as plt
from Grow_Obstacle import *
from generate_visibility import *
import sys

print 'Argument List:', str(sys.argv)

#**Global Var Definition
start = []
goal = []
world = []
obs = []
initial_obs = []
convex_obs = []
filename = str(sys.argv[1])
print 'Filename Provided is : ' + filename
#***********************************************
configurefile = open(filename,'r')

cnt = 0
obs_cnt = 0
obpts = 0
read_obs_pts = False
while True:
    line = configurefile.readline()
    paras = line.split(' ')
   # print len(paras)
    print paras[0]
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
    #print i
    initial_obs.append(obs)
    obs = []
    #print initial_obs
plt.ion()
plt.scatter((start[0],goal[0]),(start[1],goal[1]))
plt.draw()
plt.pause(0.1)
for ibos in initial_obs:
    a = []
    b = []
    for item in ibos:
        a.append(item[0])
        b.append(item[1])
    a.append(ibos[0][0])
    b.append(ibos[0][1])
    plt.plot(a, b, '.b-')
    plt.pause(0.0001)

initial_obs = my_grow_obs(start[0],start[1],0,initial_obs)
#print initial_obs
for ibos in initial_obs:
    x = []
    y = []
    for item in ibos:
        x.append(item[0])
        y.append(item[1])
#plt.show()

convex_obs = get_convex(initial_obs)
#print len(convex_obs)
for ibos in convex_obs:
    x = []
    y = []
    #print ibos
    for item in ibos:
        x.append(item[0])
        y.append(item[1])
    x.append(ibos[0][0])
    y.append(ibos[0][1])
    plt.plot(x,y,'.r-',linewidth=2)
    plt.pause(0.0001)

plt.scatter(a,b,color='red')
#plt.show()

graph = visibility_graph()

print graph.vertices
print graph.real_vertices
fin_path = graph.line_connection(convex_obs,start,goal)
#plt.show()
print fin_path
#plt.pause(20)
plt.savefig('res.jpg')
with open('Route_For_race.txt','w') as routein:
    for i in range(0, len(fin_path)):
        routein.write(str(fin_path[i][0])+','+str(fin_path[i][1])+'\n')
routein.close()