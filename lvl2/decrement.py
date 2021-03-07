from fractions import Fraction

def solution(pegs):
    dist = pegs[1]-pegs[0]
    if len(pegs) == 2 and dist > 3:
        result=Fraction('2/3')*dist
        return [result.numerator,result.denominator]
    
    radius=dist-1
    while radius >= 1 :
        candidate=assign(radius,pegs)
        first=candidate[0]
        last=candidate[-1]
        print candidate
        if first==2*last:
            return [candidate[0],1]
        radius-=1

    return([-1,-1])

def assign(radius,pegs):
    if len(pegs) == 1:
        return [radius]
    else:
        dist = pegs[1]-pegs[0]
        remaindius = dist-radius
        if remaindius >= 1:
            return([radius]+assign(remaindius,pegs[1:]))
        else:
            return [-1]

# print solution([1, 5])
print solution([4, 17, 50,60])
# print solution([4, 30, 50])