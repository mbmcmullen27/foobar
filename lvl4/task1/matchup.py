def match(a,b):
    x=a
    y=b
    history=set()
    while x!=y:
        # print('x:{} y:{}'.format(x,y))
        # print history
        if x > y:
            history.add((x,y))
            if (x-y,y*2) in history: 
                return history
            x=x-y
            y*=2
        elif y > x:
            history.add((x,y))
            # print 'x={} y={}'.format(x,y)
            if (x*2,y-x) in history: 
                return history
            y=y-x
            x*=2
        else:
            return -1

def matchlist(contender,trainers):
    candidates=[]
    for i in trainers:
        # print('x:{} y:{}'.format(contender,i))
        res=match(contender,i)
        if not res is None:
            # print res
            # candidates.append((contender,i))
            candidates.append(i)
    return candidates

def driver(banana_list):
    print banana_list
    if len(banana_list) == 1: return 1
    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]
        matches=matchlist(root,pool)
        banana_list.insert(i,root)
        # print root
        # print pool
        print '{}:{}'.format(root,matches)


# print dict(match(21,1))
# print matchlist(1,[7,3,21,13,19])
driver([7,3,21,13,19,1])
# driver([1,1])
# driver([9,10,10,20,20,79,80,100,13])
# driver([9,10,10,20,13,79,86,101,13,900,48,1,3])