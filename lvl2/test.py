def solution(pegs):
    dist = pegs[1]-pegs[0]
    
    for p in range(1,dist):
        candidate=assign(p,pegs)
        if(candidate[0]==2*candidate[-1]):
            return([candidate[0],1])

    return([-1,-1])

def assign(radius,pegs):
    if(len(pegs) == 1):
        return([radius])
    else:
        dist = abs(pegs[1]-pegs[0])
        size = dist-radius
        if size > 0:
            if(pegs==[]):
                return
            elif(isinstance(pegs,int)):
                return([radius].append(assign(size,pegs[1:])))
            else:
                return([radius]+(assign(size,pegs[1:])))
        else:
            return([-1])



print(solution([4, 30, 50]))