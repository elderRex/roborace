from numpy import *
import matplotlib.pyplot as plt

def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b
# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1 #r
    db = b2-b1 #s
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    print 'num'+str(num)
    print 'denom'+str(denom)
    print da
    print db
    print dp
    return (num / denom.astype(float))*db + b1

x = [1,2,3,4,6,7,8]
p1 = array((50, 100))
p2 = array((50, 10))
p3 = array((90, 190))
p4 = array((90, 90))

plt.plot((p1[0],p2[0]),(p1[1],p2[1]))
plt.plot((p3[0],p4[0]),(p3[1],p4[1]))
res = seg_intersect(p1,p2,p3,p4)
print res
plt.plot(res[0],res[1],'.r-')
plt.show()
def mycomp(a,b):
    if a > b:
        return -1 #a,b
    if a <= b:
        return 1 #b,a
    return 0

print sorted(x,cmp=mycomp)
