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
                if memo.get((x,y)) or (x*2,y-x) in history: 
                    return history
                y=y-x
                x*=2
            else:
                return -1

    candidates=[]
    #**most major change here, subtle, we want a list of banana_list keys for a preference list, not values
    for i in range(len(trainers)):
        res=wrestle(contender,trainers[i])
        if not res is None:
            for r in res:
                memo[r]=True
            candidates.append(i)
    return candidates

def solution(banana_list):
    if len(banana_list) == 1: return 1
    prefs=dict()
    memo=dict()
    stack=[]

    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]

        if not memo.get(root): memo[root]=matchlist(root,pool)
        prefs[i]=memo[root][:]

        #I suspect we don't need to include root anymore, we have a preference list
        stack.append(i) 
        banana_list.insert(i,root)
        

    for i in range(len(prefs)):
        print '[{}]:{}'.format(i,prefs[i])

    proposals=dict()
    leftovers=0
    
    while stack:
        print stack
        index=stack.pop(0)
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        if not pref_list: leftovers+=1
        
        while pref_list:
            p=prefs[index].pop(0)

            # print unassigned
            # print banana_list   
            # print 'p={}\nids={}\nindex={}'.format(p,ids,index)

            if not p in assigned: 
                proposals[index]=p
                pref_list.insert(0,p)
                break
            else:
                stack.insert(0,index)
                break               

    print 'proposals: {}'.format(proposals)
    # WE DONT PREFER ANYONE LESS -only remove from a list if your explicitly rejected
    # for p in range(len(proposals)):
    #     #p and proposals[p] are both indexes in banana_list and pref
    #     #remove anyone p prefers less than the current proposal (everyone)
    #     held=proposals[p]
    #     print '\n{}'.format(banana_list)
    #     # print 'i:{} holds a proposal from i:{}'.format(p,held) 
    #     if len(prefs[p]) >= 2:
    #         ids=[i for i,val in enumerate(prefs[p]) if (val == banana_list[p] or val == banana_list[held])]
    #         print 'BANL  [{}],[{}]\t: \t{} , {}'.format(p,held,banana_list[p],banana_list[held])
    #         print 'PREFS [{}]\t: \t{}'.format(p,prefs[p])
    #         print 'FILT\t\t: \t{}'.format(ids)
    #         vals=[prefs[p][i] for i in ids]
    #         print 'VALS\t\t: \t{}'.format(vals)
    #         prefs[p]=vals
    #         if not vals: leftovers+=1

            #remove p from removed preference's lists
    
    return leftovers

print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])