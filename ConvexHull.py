import math

p0 = [0,1000]

def mycomp(obptA,obptB):
    global p0
    distA = math.sqrt(pow(obptA[0] - p0[0],2)+pow(obptA[1]-p0[1],2))
    distB = math.sqrt(pow(obptB[0] - p0[0], 2) + pow(obptB[1] - p0[1], 2))
    if distA == 0:
        #A is p0, p0 > obptB
        return -1
    elif distB == 0:
        return 1
    cA = (obptA[0]-p0[0])/distA
    cB = (obptB[0]-p0[0])/distB
    #if obptA[0] == 200 or obptB[0] == 200:
    #    print distA
    if cA > cB:
        return -1 #obpta,bptb
    elif cA < cB:
        return 1
    else:
        if distA < distB:
            return -1
        if distB > distA:
            return 1
    return 0

def get_p0_sort(ob):
    global p0
    p0 = [0, 1000]
    for i in range(0,len(ob)):
        #print ob[i]
        if ob[i][1] < p0[1] and ob[i][0] > p0[0]:
            #print 'get'
            p0[1] = ob[i][1]
            p0[0] = ob[i][0]
        if ob[i][1] < p0[1]:
            p0[1] = ob[i][1]
            p0[0] = ob[i][0]
    #print p0

    fin = sorted(ob,cmp=mycomp)
    #print fin
    return (p0,fin)

def check(p0,pn_1,p_i):
    return (pn_1[0] - p0[0])*(p_i[1] - p0[1]) - (pn_1[1] - p0[1])*(p_i[0] - p0[0])

def graham(p0,sob):
    fin_ob = []
    #*******
    print 'sob[0]'+str(sob[0])
    fin_ob.append(sob[0])
    fin_ob.append(sob[1])

    i = 2
    print len(fin_ob)
    while i < len(sob):
        if check(fin_ob[len(fin_ob)-2],fin_ob[len(fin_ob)-1],sob[i]) > 0:
            fin_ob.append(sob[i])
            i += 1
        else:
            fin_ob.pop()

    return fin_ob

def get_convex(init_obs):
    convex_obs = []
    #print len(init_obs)
    for i in range(0, len(init_obs)):
        #for each obstacle
        fin_ob = []
        (p0,obseq) = get_p0_sort(init_obs[i])
        fin_ob = graham(p0,obseq)
        convex_obs.append(fin_ob)

    return convex_obs