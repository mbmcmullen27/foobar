def solution(pegs):
    dist = pegs[1]-pegs[0]
    
    for p in range(1,dist*1000):
        radius = p*0.001
        candidate=assign(radius,pegs)

        if(candidate[0]==2*candidate[-1]):
            # return simplify(candidate)
            return list(candidate[0].as_integer_ratio())

    return([-1,-1])

def simplify(candidate):
    if(int(candidate[0])==candidate[0]):
        return [int(candidate[0]),1]
    else:
        return [int(candidate[0]*2),2]

def assign(radius,pegs):
    if(len(pegs) == 1):
        return([radius])
    else:
        dist = abs(pegs[1]-pegs[0])
        size = dist-radius
        if size > 0.5:
            if(pegs==[]):
                return
            elif(isinstance(pegs,int)):
                return([radius].append(assign(size,pegs[1:])))
            else:
                return([radius]+(assign(size,pegs[1:])))
        else:
            return([-1])


# solution([2, 10, 16])
print(solution([4, 30, 50]))
        # print("--------")
        # # print(candidate)
        # # print(simplify(candidate))
        # print("--------")

        #         print("--------")
        # print(candidate)
        # print(list(candidate[0].as_integer_ratio()))
        # # print(simplify(candidate))
        # print("--------")
