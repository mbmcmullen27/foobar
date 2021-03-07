import math

def solution(n):
    pellets=long(n)
    return sift(0,pellets)
    
def sift(ops,pellets):
    if pellets and not (pellets & (pellets - 1)):
        return ops+int(math.log(pellets,2));  

    while pellets%2 == 0:
        pellets=pellets/2
        ops+=1

    if pellets == 1: return(ops)
    countleft = sift(ops+1,pellets-1)
    countright= sift(ops+1,pellets+1)

    return min(countleft,countright)

    
print solution('300')
print solution('4')
print solution('15')