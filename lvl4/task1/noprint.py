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

    for i in range(len(banana_list)):
        root=banana_list[i]
        prefs[i]=matchlist(i,banana_list)


    proposals=dict()
    leftovers=0
    
    stack=list(range(len(banana_list)))

    while stack:
        index=stack.pop(0)
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        if not pref_list: leftovers+=1
        
        while pref_list:
            p=prefs[index].pop(0)


            if not p in assigned: 
                proposals[index]=p
                pref_list.insert(0,p)
                break
            else:
                stack.insert(0,index)
                break               


    
    return leftovers

print solution([1,1])
print solution([7,3,21,13,19,1])
print solution([1,7,3,21,13,19])