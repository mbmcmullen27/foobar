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

    for i in range(len(banana_list)):
        root=banana_list[i]
        prefs[i]=matchlist(i,banana_list)


    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])

    proposals=dict()
    leftovers=0
    
    stack=list(range(len(banana_list)))
    def preferences(x):
        return len(prefs[x])
    stack=sorted(stack,key=preferences)

    while stack:
        index=stack.pop(0)
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        if not pref_list: leftovers+=1
        
        while pref_list:
            p=prefs[index][0]
            print '{}->{} : {}'.format(index,p,[banana_list[i] for i in pref_list])

            if not p in assigned: 
                proposals[index]=p
                break
            else:
                # reject=sutors[assigned.index(p)]
                # proposals[index]=p
                prefs[index].pop(0)
                # stack.insert(0,index)
                # break               
    print 'proposals: {}'.format(proposals)
    # for i in range(len(prefs)):
    #     print '[{}]:{}->{}:{}'.format(i,banana_list[i],banana_list[proposals[i]],[banana_list[k] for k in prefs.get(i)])    
    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])
    # WE DONT PREFER ANYONE LESS -only remove from a list if your explicitly rejected
    for p in range(len(proposals)):
        #p and proposals[p] are both indexes in banana_list and pref
        #remove anyone p prefers less than the current proposal (noone see line-=2 )
        held=proposals[p]
        # print '\n{}'.format(banana_list)
        # print 'i:{} holds a proposal from i:{}'.format(p,held) 
        if len(prefs[p]) >= 2:
            #check for cycles
            cycles(p,proposals,prefs)

    print 'proposals: {}'.format(proposals)

    return leftovers

def cycles(p,proposals,prefs):
    print 'checking for cycles...'
    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])
    history=dict()
    def iterate(p):
        if len(prefs[p])<=1:
            return
        
        q=prefs[p][1]

        if len(prefs[q])<=1:
            return

        suspect=prefs[q][-1]
        
        if history.get(suspect):
            prefs[suspect].pop(prefs[suspect].index(q))
            prefs[q].pop(prefs[q].index(suspect))
            #found a loop
            #pi+1 rejects qi
            print 'loop! {} rejects {}'.format(suspect,q)
        else:
            print 'p:{} -> q:{} -> q\':{}'.format(p,q,suspect)
            history[p]=True
            iterate(suspect)
        
    iterate(p)


# print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])
print solution([1,7,3,21,13,19])