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
        
    proposals=dict()
    leftovers=0

    print banana_list
    while stack:
        sutor=stack.pop(0)        # (id,value,preferences])
        index=sutor[0]
        pref_list=prefs[index]
        assigned=proposals.values()
        sutors=proposals.keys()
        print stack
        print 'sutors: {}'.format(sutors)
        print 'proposals: {}'.format(proposals)
        if not pref_list: leftovers+=1
        
        while pref_list:
            # print stack
            p=prefs[index].pop(0)
            ids=[i for i,val in enumerate(banana_list) if val == p]

            unassigned= filter(lambda i: not i in assigned,ids)
            print unassigned
            print stack
            print banana_list   
            print 'p={}\nids={}\nindex={}'.format(p,ids,index)
            print 'proposals: {}'.format(proposals)
            
            if unassigned:
                uid=unassigned.pop(0)
                proposals[index]=uid
                pref_list.insert(0,p)
                print 'uid: {} selected from: {}'.format(uid,ids)
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

            # for i in ids:
            #     previous=sutors[assigned.index(i)]
            #     # print 'id: {}'.format(i)
            #     # print 'previous: {}'.format(previous)
            #     # print 'sutors: {}'.format(sutors)
            #     if length[previous]>length[index]:
            #         proposals[index]=i
            #         proposals[previous]=None
            #         stack.insert(0,(previous,banana_list[previous])
            #         pref_list.insert(0,p)
            #         break

                    
        print 'proposal values: \t{}'.format(list(map(lambda i : banana_list[i],proposals.values())))
        print 'banana_list: \t\t{}'.format(banana_list)
            # if p in assigned:
            #     previous=sutors[assigned.index(p)]

            #     # matches need to check if they exist in eachother's preference list now
            #     if length[previous] > length[sutor[1]] :
            #         # proposals is absorbing duplicates here
            #         # may need to track sutors by index from 'banana_list' throughout
            #         proposals[sutor[0]]=p
            #         stack.insert(0,sutors[assigned.index(p)])
            #         pref_list.insert(0,p)
            #         break
            # else:
            #     proposals[sutor[0]]=p
            #     pref_list.insert(0,p)
            #     break

    return leftovers

print solution([1,1])
# print solution([7,3,21,13,19,1])
# print solution([7,3,21,7,13,19,1])
# print solution([9,10,10,20,13,79,86,101,13,900,48,1,3])