# from collections import OrderedDict

def matchlist(contender,trainers):
    memo=dict()
    def wrestle(a,b):
        x=a
        y=b
        history=set()
        while x!=y:
            if x > y:
                history.add((x,y))
                if memo.get((x,y)) or (x-y,y*2) in history: 
                    return history
                x=x-y
                y*=2
            elif y > x:
                history.add((x,y))
                if memo.get((x,y)) (x*2,y-x) in history: 
                    return history
                y=y-x
                x*=2
            else:
                return -1

    candidates=[]
    for i in trainers:
        res=wrestle(contender,i)
        if not res is None:
            candidates.append(i)
    return candidates

def solution(banana_list):
    print banana_list
    print
    if len(banana_list) == 1: return 1
    prefs=dict()
    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]
        matches=matchlist(root,pool)
        banana_list.insert(i,root)
        prefs[str(root)]=matches
        # print '{}:{}'.format(root,matches)
        # duplicate banana key values need to work dummy ie [1,1]
    
    for i in prefs:
        print '{}:{}'.format(i,prefs[i])

    sorted_list=sorted(prefs.values(),key=len)
    length=dict()
    stack=[]
    # print sorted_list
    for i in sorted_list:
        for k in prefs.keys():
            if prefs[k] == i:
                length[k] = len(prefs[k])
                stack.append(k)
                break
    print
    print str(length)
    print stack
    proposals=dict()
    while stack:
        sutor=stack.pop(0)
        pref_list=prefs[sutor]
        assigned=proposals.values()
        sutors=proposals.keys()
        while pref_list:
            p=pref_list.pop(0)
            #propose to next candidate
            print 'proposals {}'.format(proposals)
            print 'sutor: {} proposing to p: {}'.format(sutor,p)
            if p in assigned:
                previous=sutors[assigned.index(p)]
                if length[previous] > length[sutor] :
                #accepting a better proposal reject the old sutor by placing them back on the stack
                    proposals[sutor]=p
                    stack.insert(0,sutors[assigned.index(p)])
                    pref_list.insert(0,p)
                    break
                else:
                    print 'rejected'
            else:
                proposals[sutor]=p
                pref_list.insert(0,p)
                break

    print proposals
    leftovers=0
    for i in prefs:
        if not prefs[i]: leftovers+=1
        print '{}:{}'.format(i,prefs[i])
    print('leftovers: {}'.format(leftovers))
    return leftovers

solution([1,1])
# solution([7,3,21,13,19,1])
# solution([9,10,10,20,13,79,86,101,13,900,48,1,3])