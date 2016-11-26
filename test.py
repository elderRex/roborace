x = [1,2,3,4,6,7,8]

def mycomp(a,b):
    if a > b:
        return -1 #a,b
    if a <= b:
        return 1 #b,a
    return 0

print sorted(x,cmp=mycomp)
