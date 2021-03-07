def solution(n):
    pellets=int(n)
    return sift(0,pellets)
    
def sift(ops,pellets):
    while pellets>1:
        if pellets%2 == 0:
            pellets=pellets/2
            ops+=1
        else:
            countleft = sift(ops+1,pellets-1)
            countright= sift(ops+1,pellets+1)
            if countleft<=countright :
                ops+=countleft
                print('going left ops:{} pelletCount:{}\n'.format(ops,pellets))
            else:
                ops+=countright
                print('going right ops:{} pelletCount:{}\n'.format(ops,pellets))
    return (ops)

print(solution('15'))
print(solution('4'))