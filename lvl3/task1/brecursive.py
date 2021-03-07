def solution(n):
    # sys.setrecursionlimit(310)
    pellets=long(n)
    return sift(pellets)
    
def sift(pellets):
    if pellets == 1: return 0
    if pellets%2 == 0:
        return 1+sift(pellets/2)
    else:
        countleft = sift(pellets-1)
        countright= sift(pellets+1)
    
        return(1+min(countleft,countright))
        
print solution('9'*250)
print solution('300')
print solution('4')
print solution('15')