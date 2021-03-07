def solution(pegs):
    dist = pegs[1]-pegs[0]
    i=dist*100
    while i >= 1:
        radius = i*0.01
        candidate=assign(radius,pegs)
        first=candidate[0]
        last=candidate[-1]
        if( first == 2*last and first != last):
            return list(candidate[0].as_integer_ratio())
        i-=1
    return([-1,-1])

def assign(radius,pegs):
    result=[]
    i=0
    while i < len(pegs)-1:
        dist = pegs[i+1]-pegs[i]
        remaindius = dist-radius        
        if remaindius < 1:
            return([-1.0])
        else:
            result+=[radius]
        i+=1
    return result

# print(solution([1,5]))
print(solution([4, 100, 500]))


    #    print("--------")
    #     print(list(candidate[0].as_integer_ratio()))
    #     print(candidate)
    #     print(candidate[0],candidate[-1])
    #     print(format(candidate[0], '.2f'))
    #     print(format(2*candidate[-1], '.2f'))
    #     print("--------")
    #     first=format(candidate[0], '.2f')
    #     last=format(candidate[-1], '.2f')