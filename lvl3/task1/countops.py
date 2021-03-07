def solution(n):
    pellets=long(n[:309])
    return sift(0,pellets)[0]
    
def sift(ops,pellets):
    while pellets>1:
        print('p:{} o:{}'.format(pellets,ops))
        if pellets%2 == 0:
            pellets=pellets/2
            ops+=1
        else:
            print('\ngoing left')
            countleft = sift(ops+1,pellets-1)
            print('\ngoing right')
            countright= sift(ops+1,pellets+1)
            if countleft[0]<countright[0] :
                ops+=countleft[0]
                pellets=countleft[1]
            else:
                ops+=countright[0]
                pellets=countright[1]
                
    return (ops,pellets)
    

print solution('300')
# print solution('4')