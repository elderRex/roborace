'''
def intersect_judge(self, vertex_1, vertex_2, vertex):
    left_x = vertex_1[0]
    left_y = vertex_1[1]
    right_x = vertex_2[0]
    right_y = vertex_2[1]
    # calculate the k and b of the line
    res = False
    if left_x != right_x:
        k1 = (right_y - left_y) / (right_x - left_x)
        b1 = right_y - k1 * right_x
        for p in range(0, len(vertex)):
            for i in range(0, len(vertex[p])):
                if i == len(vertex[p]) - 1:
                    j = 0
                else:
                    j = i + 1
                x_1 = vertex[p][i][0]
                y_1 = vertex[p][i][1]
                x_2 = vertex[p][j][0]
                y_2 = vertex[p][j][1]
                # y1_line = k * x_1 + b
                # y2_line = k * x_2 + b
                # if (y_1 - y1_line) * (y_2 - y2_line) < 0:
                if x_1 != x_2:
                    k2 = (y_2 - y_1) / (x_2 - x_1)
                    b2 = y_2 - k2 * x_2
                    if k2 != k1:
                        x0 = (b2 - b1) / (k2 - k1)
                        y0 = k1 * x0 + b1
                        if (x0 >= min(left_x, right_x) and x0 <= max(left_x, right_x) and y0 >= min(left_y,
                                                                                                    right_y) and y0 <= max(
                                right_y, left_y)):
                            return True
                    else:
                        if (x_1 >= min(left_x, right_x) and x_1 <= max(left_x, right_x) and y_1 >= min(left_y,
                                                                                                       right_y) and y_1 <= max(
                                left_y, right_y)) or (
                                        x_2 >= min(left_x, right_x) and x_2 <= max(left_x, right_x) and y_2 >= min(
                                    left_y, right_y) and y_2 <= max(left_y, right_y)):
                            return True
                else:
                    x0 = x_1
                    y0 = k1 * x0 + b1
                    if (x0 >= min(left_x, right_x) and x0 <= max(left_x, right_x)):
                        return True
    else:
        for p in range(0, len(vertex)):
            for i in range(0, len(vertex[p])):
                if i == len(vertex[p]) - 1:
                    j = 0
                else:
                    j = i + 1
                x_1 = vertex[p][i][0]
                y_1 = vertex[p][i][1]
                x_2 = vertex[p][j][0]
                y_2 = vertex[p][j][1]
                # if (x_1 - left_x) * (x_2 - left_y) < 0:
                if x_1 != x_2:
                    k2 = (y_2 - y_1) / (x_2 - x_1)
                    b2 = y_2 - k2 * x_2
                    x0 = left_x
                    y0 = k2 * x0 + b2
                    if x0 >= min(left_x, right_x) and x0 <= max(left_x, right_x) and y0 >= min(left_y,
                                                                                               right_y) and y0 <= max(
                            left_y, right_y):
                        return True
                else:
                    if (y_1 >= min(left_y, right_y) and y_1 <= max(left_y, right_y)) or (
                            y_2 >= min(left_y, right_y) and y_2 <= max(left_y, right_y)):
                        return True

    return res

        def intersect_judge(self, vertex_1, vertex_2,convex_ob):
        # calculate the k and b of the line
        res = False
        for p in range(0,len(convex_ob)):
            for i in range(0, len(convex_ob[p])):
                if i == len(convex_ob[p]) - 1:
                    j = 0
                else:
                    j = i + 1
                if vertex_1 == convex_ob[p][i] and vertex_2 == convex_ob[p][j]: #if the line is part of the obstacle
                    return False
                #otherwise, check for intersection
                da = np.array((vertex_2[0]-vertex_1[0], vertex_2[1]-vertex_1[1]))
                db = np.array((convex_ob[p][j][0]-convex_ob[p][i][0],convex_ob[p][j][1]-convex_ob[p][i][1]))
                dp = np.array((vertex_1[0]-convex_ob[p][i][0],vertex_1[1]-convex_ob[p][i][1]))
                dap = perp(da)
                denom = dot(dap, db)
                num = dot(dap, dp)
                if denom == 0:
                    if num == 0:
                        #paralle and overlap, means ok to go
                        return False
                    else:
                        #paralle but does not overlap, no intersection
                        return False
                else:
                    #not parallel, has intersection
                    pseg = (num / denom.astype(float)) * db + convex_ob[p][i]
                    minv = min(convex_ob[p][i][0],convex_ob[p][j][0])
                    maxv = max(convex_ob[p][i][0],convex_ob[p][j][0])
                    print pseg
                    if pseg[0] > minv and pseg[0] < maxv:
                        print "caught"
                        return True
        return res
'''