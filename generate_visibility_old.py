import heapq
import sys
import math

class visibility_graph:


    def __init__(self):
        self.real_vertices = []
        self.vertices = {}
        print "OKIE"


    def intersect_judge(self, vertex_1, vertex_2,vertex):
        left_x = vertex_1[0]
        left_y = vertex_1[1]
        right_x = vertex_2[0]
        right_y = vertex_2[1]
        # calculate the k and b of the line
        res = False
        if left_x != right_x:
            k = (right_y - left_y) / (right_x - left_x)
            b = right_y - k * right_x
            for p in range(0,len(vertex)):
                for i in range(0, len(vertex[p])):
                    if i == len(vertex[p]) - 1:
                        j = 0
                    else:
                        j = i + 1
                    x_1 = vertex[p][i][0]
                    # y_1 = vertex[i][1]
                    x_2 = vertex[p][j][0]
                    # y_2 = vertex[j][1]
                    if (k * x_1 + b) * (k * x_2 + b) < 0:
                        return True
        else:
            for p in range(0, len(vertex)):
                for i in range(0, len(vertex[p])):
                    if i == len(vertex[p]) - 1:
                        j = 0
                    else:
                        j = i + 1
                    x_1 = vertex[p][i][0]
                    # y_1 = vertex[i][1]
                    x_2 = vertex[p][j][0]
                    # y_2 = vertex[j][1]
                    if (x_1 - left_x) * (x_2 - left_y) < 0:
                        return True
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


    def dijkstras_algorithm(self, start, goal):
        distance = {}  # Distance from start to node
        pre_node = {}  # pre_node node in optimal path from source
        nodes = []  # Priority queue of all nodes in Graph
        print self.vertices
        print start
        print goal
        for vertex in self.vertices:  # create vertex set Q
            if vertex == start:
                distance[vertex] = 0
                heapq.heappush(nodes, [0, vertex])  # Q
            else:
                distance[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            pre_node[vertex] = None

        while nodes:
            u = heapq.heappop(nodes)[1]
            if u == goal:  # If the closest node is our target we're done so print the path
                path = []
                while pre_node[u]:  # Traverse through nodes til we reach the root which is 0
                    path.append(u)
                    u = pre_node[u]
                return path
            for neighbor in self.vertices[u]:  # Look at all the nodes that this vertex is attached to
                alt = distance[u] + self.vertices[u][neighbor]  # Alternative path distance
                if alt < distance[neighbor]:  # If there is a new shortest path update our priority queue (relax)
                    distance[neighbor] = alt
                    pre_node[neighbor] = u
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        print pre_node
        return distance


    def __str__(self):
        return str(self.vertices)


    def line_connection(self, vertex, start, goal):
        self.converse(vertex,start,goal)
        for i in range(0, len(self.real_vertices)):
            vertex_temp = {}
            x_1 = self.real_vertices[i][0]
            y_1 = self.real_vertices[i][1]
            for j in range(i, len(self.real_vertices)):
                x_2 = self.real_vertices[j][0]
                y_2 = self.real_vertices[j][1]
                # add parameters
                if j == 1:
                    j = 1
                result = self.intersect_judge((x_1,y_1),(x_2,y_2),vertex)
                if result == True:
                    continue
                else:
                    distance_temp = math.sqrt(pow(x_1 - x_2,2) + pow(y_1 - y_2, 2))
                    vertex_temp[str(j)] = distance_temp
            self.add_vertex(str(i), vertex_temp)
        return self.dijkstras_algorithm(str(0),str(1))






