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
    memo=dict()
    stack=[]

    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]

        if not memo.get(root): memo[root]=matchlist(root,pool)
        prefs[i]=memo[root][:]

        stack.append((i,root))
        banana_list.insert(i,root)
        
    proposals=dict()
    leftovers=0

    while stack:
        sutor=stack.pop(0)                
        index=sutor[0]
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        if not pref_list: leftovers+=1
        
        while pref_list:
            p=prefs[index].pop(0)
            ids=[i for i,val in enumerate(banana_list) if val == p]

            unassigned= filter(lambda i: not i in assigned,ids)

            if unassigned: 
                uid=unassigned.pop(0)
                proposals[index]=uid
                pref_list.insert(0,p)
                break
            else:
                stack.insert(0,(index,banana_list[index]))
                break               

    for p in range(len(proposals)):
        held=proposals[p]
        if len(prefs[p]) >= 2:
            ids=[i for i,val in enumerate(prefs[p]) if (val == banana_list[p] or val == banana_list[held])]
            vals=[prefs[p][i] for i in ids]
            prefs[p]=vals
            if not vals: leftovers+=1

    for p in range(len(proposals)):
        held=proposals[p]
    return leftovers

# print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])
print solution([1,1])
# print solution([7,3,21,13,19,1])

# proposals: {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4, 6: 8, 7: 6, 8: 7, 9: 10, 10: 9}
