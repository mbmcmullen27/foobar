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
    for i in range(len(bananas)):
        if i <> challenger:
            res=wrestle(bananas[challenger],bananas[i])
            if not res is None:
                for r in res:
                    memo[r]=True
                candidates.append(i)
    return candidates

def solution(banana_list):
    if len(banana_list) == 1: return 1
    prefs=dict()

    def preferences(x):
        return len(prefs[x])
    
    for i in range(len(banana_list)):
        root=banana_list[i]
        prefs[i]=matchlist(i,banana_list)

    for i in range(len(prefs)):
        prefs[i]=sorted(prefs[i],key=preferences)

    proposals=dict()    
    stack=list(range(len(banana_list)))    
    stack=sorted(stack,key=preferences,reverse=True)


    blocking=0
    while stack and len(proposals)<len(banana_list):
        p=stack.pop(0)
        pref_list=prefs[p]
        assigned=proposals.values()
        sutors=proposals.keys()

        if p in assigned: continue
        if not pref_list: 
            blocking+=1
        else:
            q=prefs[p][0]
            if q in assigned: 
                reject=sutors[assigned.index(q)]
                proposals.pop(reject)

                prefs[reject].pop(0)
                stack.insert(0,reject)                    

            proposals[p]=q
            proposals[q]=p

    return blocking


print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])