
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
    for i in trainers:
        res=wrestle(contender,i)
        if not res is None:
            for r in res:
                memo[r]=True
            candidates.append(i)
    return candidates

def solution(banana_list):
    if len(banana_list) == 1: return 1
    prefs=dict()
    instances=dict()
    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        if not instances.get(root): 
            instances[root]=1
        else:
            instances[root]+=1
        
        pool=banana_list[:]
        matches=matchlist(root,pool)
        banana_list.insert(i,root)
        prefs[root]=matches

    sorted_list=sorted(prefs.values(),key=len)
    length=dict()
    stack=[]
    for i in sorted_list:
        for k in prefs.keys():
            if prefs[k] == i:
                length[k] = len(prefs[k])
                for i in range (instances[k]):
                    stack.append((i+i,k,prefs[k]))
                break
    proposals=dict()
    leftovers=0

    while stack:
        sutor=stack.pop(0)
        pref_list=sutor[2][0:]
        
        ## proposal values are not unique 
        assigned=proposals.values()
        sutors=proposals.keys()

        if not pref_list: leftovers+=1
        while pref_list:
            p=pref_list.pop(0) # how do we match a preference to an index now?

            #p will already exist in assigned if there exists more 
            # than 1 trainer with the same start value
            if p in assigned:
                previous=sutors[assigned.index(p)]

                # matches need to check if they exist in eachother's preference list now
                if p in pref_list and length[previous] > length[sutor[1]] :
                    # proposals is absorbing duplicates here
                    # may need to track sutors by index from 'banana_list' throughout
                    proposals[sutor[0]]=p
                    stack.insert(0,sutors[assigned.index(p)])
                    pref_list.insert(0,p)
                    break
            else:
                proposals[sutor[0]]=p
                pref_list.insert(0,p)
                break

    return leftovers

# print solution([7,3,21,13,19,1])
print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])