from fractions import Fraction

def solution(pegs):
    dist = pegs[1]-pegs[0]

    if len(pegs) == 2 and dist >= 3:
        result=Fraction('2/3')*dist
        return [result.numerator,result.denominator]

    i=(3*dist)-1
    while i >= 3 :
        radius = i*Fraction('1/3')
        candidate=assign(radius,pegs)
        first=candidate[0]
        last=candidate[-1]
        if first==2*last and last >= 1:
            return [candidate[0].numerator,candidate[0].denominator]
        i-=1

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


def printDistance(pegs):
    i=0
    distances=[None]*(len(pegs)-1)
    while i < len(pegs)-1:
        distances[i]=pegs[i+1]-pegs[i]
        i+=1

    print('{}\n'.format(distances))

# print solution([4, 30, 50])
# print solution([10,20,30,40])
print('---------------')
print solution([4, 17, 50])
print('---------------')
print solution([4, 33, 50])
print('---------------')
print solution([4, 17, 50, 85])
print('---------------')
print solution([4, 17, 50, 100])
print('---------------')
print solution([5, 17, 50, 100, 128])
print('---------------')
print solution([1, 10])
# print solution([10,26,45,60])