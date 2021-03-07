from decimal import Decimal
def solution(pegs):
    dist = pegs[1]-pegs[0]
    for p in range(dist*100):
        radius = p*Decimal(0.01)+1
        candidate=assign(radius,pegs)
        first=candidate[0]
        last=candidate[-1]

        print("--------")
        print(list(candidate[0].as_integer_ratio()))
        print(candidate)
        print(candidate[0],candidate[-1])
        print(format(candidate[0], '.2f'))
        print(format(2*candidate[-1], '.2f'))
        print("--------")

        if Decimal(first)==2*Decimal(last):
            return list(candidate[0].as_integer_ratio())

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
            return([-1.0])



print(solution([4, 100, 500]))