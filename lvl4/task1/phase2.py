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
    length=dict()
    memo=dict()
    stack=[]

    for i in range(len(banana_list)):
        root=banana_list.pop(i)
        pool=banana_list[:]

        if not memo.get(root): memo[root]=matchlist(root,pool)
        prefs[i]=memo[root][:]
        length[i] = len(prefs[i])

        stack.append((i,root))
        banana_list.insert(i,root)
    print prefs
    proposals=dict()
    leftovers=0

    while stack:
        print stack
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
            print unassigned
            print banana_list   
            print 'p={}\nids={}\nindex={}'.format(p,ids,index)
            print 'proposals: {}'.format(proposals)
            if unassigned:
                uid=unassigned.pop(0)
                proposals[index]=uid
                pref_list.insert(0,p)
                break
            else:
                for i in ids:
                    previous=sutors[assigned.index(i)]
                    if length[previous] > length[index] :
                        proposals[index]=i
                        proposals.pop(previous)
                        stack.insert(0,(previous,banana_list[previous]))
                        pref_list.insert(0,p)
                        break
                    else:
                        stack.insert(0,(index,banana_list[index]))

                break

                                                                        
                                                                                                                                                     
    return leftovers

# print solution([1,1])
print solution([7,3,21,13,19,1])
# print solution([7,3,21,7,13,19,1])
# print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])