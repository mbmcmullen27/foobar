import math

def solution(n):
    pellets = int(n)

    # if pellets and not (pellets & (pellets - 1)):
    #     return math.log(pellets,2);

    nextPower = powerUp(pellets)
    lastPower = powerDown(pellets)
    distUp = nextPower - pellets
    distDown = pellets - lastPower
    
    print('Powers ^{} v{}'.format(nextPower,lastPower))

    a=distUp+math.log(nextPower,2)
    b=distDown+math.log(lastPower,2)
    return int(min(a,b))

def powerUp(n):
    if n and not (n & (n - 1)):
        return n;  

    count=0
    nextPower=1
    
    while n!=0 :
        n >>= 1
        count += 1

    return 1<<count


def powerDown(n):
    lastPower = int(math.log(n, 2))
    return int(pow(2, lastPower)) 

print solution('15')
print solution('4')
print(solution('300'))