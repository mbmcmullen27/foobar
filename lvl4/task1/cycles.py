def matchlist(challenger,bananas):
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
                if memo.get((x,y)) or (x*2,y-x) in history: 
                    return history
                y=y-x
                x*=2
            else:
                return None

    candidates=[]
    #**most major change here, subtle, we want a list of banana_list keys for a preference list, not values
    #wrong, bananas is banana_list with target removed incorrect indexs getting put into lists
    for i in range(len(bananas)):
        if i <> challenger:
            res=wrestle(bananas[challenger],bananas[i])
            if not res is None:
                for r in res:
                    memo[r]=True
                candidates.append(i)
    return candidates

def solution(banana_list):
    print banana_list
    if len(banana_list) == 1: return 1
    prefs=dict()

    def preferences(x):
        return len(prefs[x])
    
    for i in range(len(banana_list)):
        root=banana_list[i]
        prefs[i]=matchlist(i,banana_list)


    for i in range(len(prefs)):
        prefs[i]=sorted(prefs[i],key=preferences)
        print '[{}]:{}'.format(i,prefs[i])

    proposals=dict()
    leftovers=0
    
    stack=list(range(len(banana_list)))
    
    stack=sorted(stack,key=preferences,reverse=True)

    while stack:
        print stack
        index=stack.pop(0)
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        if not pref_list: leftovers+=1
        for i in range(len(prefs)):
            print '\t[{}]:{}'.format(i,prefs[i])
        
        if pref_list :
            p=prefs[index][0]
            # print '{}->{} : {}'.format(index,p,[banana_list[i] for i in pref_list])
            print '{}->{} '.format(index,p)

            if not p in assigned: 
                print 'ACCEPT'
                proposals[index]=p
            else:
                # decide who to reject based on p's preference
                # if index is higher on p's list reject the trainer p is assigned too
                reject=sutors[assigned.index(p)]
                print '{} HOLDS {}'.format(reject,p)
                # if prefs[p].index(reject)>prefs[p].index(index):
                proposals[index]=p
                proposals.pop(reject)
                print '{} REJECTS {}'.format(p,reject)
                prefs[p].pop(prefs[p].index(reject))
                prefs[reject].pop(0)
                stack.insert(0,reject)
                # else:
                #     print '{} REJECTS {}'.format(p,index)
                #     prefs[index].pop(0)
                #     stack.insert(0,index)               
        print proposals
            
    print 'proposals: {}'.format(proposals)
    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])

    for p in range(len(proposals)):
        held=proposals[p]
        # print '\n{}'.format(banana_list)
        # print 'i:{} holds a proposal from i:{}'.format(p,held) 
        # if len(prefs[p]) >= 2:
            #check for cycles
            # cycles(p,proposals,prefs)

    print 'proposals: {}'.format(proposals)

    return leftovers

def cycles(p,proposals,prefs):
    print 'checking for cycles...'
    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])
    history=dict()
    # def iterate(p):
    #    iterate(p)


# print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])
print solution([1,7,3,21,13,19])