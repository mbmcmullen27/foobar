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
    stack=list(range(len(banana_list)))    
    stack=sorted(stack,key=preferences,reverse=True)

    def phaseOne(stack):
        leftovers=0
        print '------------BEGIN PHASE ONE------------'
        print stack
        while stack and len(proposals)<len(banana_list):
            p=stack.pop(0)
            pref_list=prefs[p]
            assigned=proposals.values()
            sutors=proposals.keys()
            if not pref_list: 
                print '{} BLOCKS: {}'.format(p,pref_list)
                leftovers+=1
            else:
                q=prefs[p][0]
                print '{}->{} '.format(p,q)
                if q in assigned: 
                    reject=sutors[assigned.index(q)]
                    # print '{} HOLDS {}'.format(reject,q)
                    # print '{} REJECTS {}'.format(q,reject)
                    # proposals.pop(reject)
                    # prefs[reject].pop(0)
                    # stack.insert(0,reject)
                    
                    print '{} HOLDS {}'.format(reject,q)
                    print '{} REJECTS {}'.format(q,p)
                    prefs[p].pop(0)
                    prefs[q].pop(prefs[q].index(p))
                    stack.insert(0,p)
                else:
                    proposals[p]=q

                # for k in prefs[q]:
                #     prefs[q].pop(prefs[q].index(k))

                for i in range(len(prefs)):
                    print '[{}]:{}'.format(i,prefs[i])

            print 'proposals: {}'.format(proposals)
        print '------------END PHASE ONE------------'
        return leftovers

    def phaseTwo(p):
        print '------------BEGIN PHASE TWO------------'
        print 'p:{}'.format(p)


        history=dict()
        def check(p):
            if len(prefs[p])<=1:
                print 'p:{} has short list (len<=1), returning...'.format(p)
                return
            
            q=prefs[p][1]

            if len(prefs[q])<=1:
                print 'q:{} has a short list (len<=1), returning...'.format(q)
                return

            suspect=prefs[q][-1]
            
            if history.get(suspect):
                prefs[suspect].pop(prefs[suspect].index(q))
                prefs[q].pop(prefs[q].index(suspect))
                #found a loop
                #pi+1 rejects qi
                print 'loop! {} rejects {}'.format(suspect,q)
                for i in range(len(prefs)):
                    print '[{}]:{}'.format(i,prefs[i])
            else:
                print 'p:{} -> q:{} -> q\':{}'.format(p,q,suspect)
                history[p]=True
                check(suspect)
        
        check(p)
        print '------------END PHASE TWO------------'

    result=phaseOne(stack)
    # for i in range(len(prefs)):
    #     print '[{}]:{}'.format(i,prefs[i])
    # print 'proposals: {}'.format(proposals)
    # print 'leftovers: {}'.format(result)

    def lengths(x):
        if len(prefs[x])>1:
            return x

    # while filter(lengths,prefs):
    # for x in range(2):
    #     for i in range(len(proposals)):
    #         phaseTwo(i)
    #         print 'proposals: {}'.format(proposals)
            
    print 'leftovers: {}'.format(result)



# solution([1,7,3,21,13,19])
# solution([1,1])
# solution([7,3,21,13,19,1])
solution([7,3,21,7,13,19,1])
# solution([9,10,10,20,13,79,86,101,13,900,48,1,3])