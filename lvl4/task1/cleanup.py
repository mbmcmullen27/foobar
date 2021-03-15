def solution(banana_list):
    if len(banana_list) == 1: return 1
    prefs=dict()
    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]
        matches=matchlist(root,pool)
        banana_list.insert(i,root)
        prefs[str(root)]=matches
    
    sorted_list=sorted(prefs.values(),key=len)
    length=dict()
    stack=[]
    for i in sorted_list:
        for k in prefs.keys():
            if prefs[k] == i:
                length[k] = len(prefs[k])
                stack.append(k)
                break
    proposals=dict()
    while stack:
        sutor=stack.pop(0)
        pref_list=prefs[sutor]
        assigned=proposals.values()
        sutors=proposals.keys()
        while pref_list:
            p=pref_list.pop(0)
            if p in assigned:
                previous=sutors[assigned.index(p)]
                if length[previous] > length[sutor] :
                    proposals[sutor]=p
                    stack.insert(0,sutors[assigned.index(p)])
                    pref_list.insert(0,p)
                    break
            else:
                proposals[sutor]=p
                pref_list.insert(0,p)
                break

    leftovers=0
    for i in prefs:
        if not prefs[i]: leftovers+=1
    return leftovers
    
def matchlist(contender,trainers):
    def wrestle(a,b):
        x=a
        y=b
        history=set()
        while x!=y:
            if x > y:
                history.add((x,y))
                if (x-y,y*2) in history: 
                    return history
                x=x-y
                y*=2
            elif y > x:
                history.add((x,y))
                if (x*2,y-x) in history: 
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

print solution([7,3,21,13,19,1])
print solution([1,1])
# solution([9,10,10,20,13,79,86,101,13,900,48,1,3])