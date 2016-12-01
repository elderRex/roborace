import heapq
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.path as mpt
from line_judge import *
import numpy as np

class visibility_graph:


    def __init__(self):
        self.real_vertices = []
        self.vertices = {}
        print "OKIE"

    def get_binary_poits(self,top,bot):
        points = []
        binary_cnt = 6
        self.getb_points(points,top,bot,binary_cnt)
        return points

    def getb_points(self,points,top,bot,cnt):
        if cnt != 0:
            mid = (top+bot)/2
            points.append(mid)
            self.getb_points(points,top,mid,cnt-1)
            self.getb_points(points, mid, bot, cnt - 1)
        else:
            return


    def intersect_judge(self, vertex_1, vertex_2,convex_ob):
        # calculate the k and b of the line
        res = False
        for p in range(0,len(convex_ob)):
            for i in range(0,len(convex_ob[p])):
                if i == len(convex_ob[p])-1:
                    j = 0
                else:
                    j = i + 1
                if vertex_1 == convex_ob[p][i] and vertex_2 == convex_ob[p][j]:
                    return False
            ob_path = mpt.Path(np.array(convex_ob[p]))
            points = self.get_binary_poits(np.array(vertex_1),np.array(vertex_2))
            for i in range(0,len(points)):
                if ob_path.contains_point(points[i]):
                    res = True
        return res
        


    def converse(self, vertex, start, goal):
        res = []
        res.append(start)
        res.append(goal)
        for i in range(0, len(vertex)):
            for j in range(0, len(vertex[i])):
                res.append(vertex[i][j])
        self.real_vertices = res


    def add_vertex(self, name, edge_dist):
        self.vertices[name] = edge_dist

    def mycomp(self,verA, verB):

        if verA[1] < verB[1]:
            # A,B
            return -1
        elif verA[1] >= verB[1]:
            # B,A
            return 1

        return 0

    def dijkstras_algorithm(self, start, goal):
        distance = {}  # Distance from start to node
        pre_node = {}  # pre_node node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph
        print self.vertices
        for vertex in self.vertices:  # create vertex set Q
            #print vertex
            if vertex == start:
                distance[vertex] = 0
                nodes.append((vertex,distance[vertex]))
                pre_node[vertex] = None
            else:
                distance[vertex] = sys.maxsize
                nodes.append((vertex, distance[vertex]))
                pre_node[vertex] = None

        print distance['0']
        Q = sorted(nodes, cmp=self.mycomp)
        while Q:
            #print Q
            Q = sorted(Q,cmp=self.mycomp)
            u = Q[0][0]
            #print Q[0]
            del Q[0]
            #print distance['1']
            #print 'this u : '+u
            #print self.vertices[u]
            for v in self.vertices[u]:  # Look at all the nodes that this vertex is attached to
                #print '(' + v + ',' + u + ')'
                alt = distance[u] + self.vertices[u][v]  # Alternative path distance
                #print alt
                if alt < distance[v]:  # If there is a new shortest path update our priority queue (relax)
                    distance[v] = alt
                    for i in range(0,len(Q)):
                        if Q[i][0] == v:
                            del Q[i]
                            Q.append((v,alt))
                            break
                    #print '('+v+','+u+')'
                    #print alt
                    pre_node[v] = u
        path = []
        u = '1'
        while pre_node[u]:  # Traverse through nodes til we reach the root which is 0
            path.append(u)
            u = pre_node[u]
        print path
        return path


    def __str__(self):
        return str(self.vertices)


    def line_connection(self, vertex, start, goal):
        print "in new line"
        self.converse(vertex,start,goal)
        print self.real_vertices[0]
        print self.real_vertices[1]
        for i in range(0, len(self.real_vertices)):
            vertex_temp = {}
            x_1 = self.real_vertices[i][0]
            y_1 = self.real_vertices[i][1]
            for j in range(0, len(self.real_vertices)):
                x_2 = self.real_vertices[j][0]
                y_2 = self.real_vertices[j][1]
                # add parameters
                if j == 21:
                    j = 21
                result = self.intersect_judge((x_1,y_1),(x_2,y_2),vertex)
                if result == True:
                    continue
                else:
                    plt.plot((x_1,x_2),(y_1,y_2),'.g-')
                    #plt.pause(0.0001)
                    distance_temp = math.sqrt(pow(x_1 - x_2,2) + pow(y_1 - y_2, 2))
                    vertex_temp[str(j)] = distance_temp
            #print vertex_temp
            self.add_vertex(str(i), vertex_temp)
        #plt.show()
        path = self.dijkstras_algorithm(str(0),str(1))
        print path
        real_path = []
        real_path.append(self.real_vertices[0])
        for i in range(0,len(path)):
            real_path.append(self.real_vertices[int(path[len(path)-1-i])])
        for i in range(0,len(real_path)-1):
            j = i + 1
            plt.plot((real_path[i][0],real_path[j][0]),(real_path[i][1],real_path[j][1]),'.y--',linewidth=4)
            #plt.pause(0.0001)

        return real_path






