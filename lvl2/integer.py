def solution(pegs):
    dist = pegs[1]-pegs[0]
    for p in range(1,dist):
        radius = p
        candidate=assign(radius,pegs)
        first=candidate[0]
        last=candidate[-1]
        if first==2*last and last >= 1:
            return [candidate[0],1]

    return([-1,-1])

def assign(radius,pegs):
    if len(pegs) == 1:
        return([radius])
    else:
        dist = pegs[1]-pegs[0]
        remaindius = dist-radius
        if remaindius >= 1:
            return([radius]+assign(remaindius,pegs[1:]))
        else:
            return([-1])