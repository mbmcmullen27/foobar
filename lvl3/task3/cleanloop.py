def solution(m,f):
    memo=dict()
    def cycle(cursor,m,f):

        macs=cursor['m']
        facs=cursor['f']

        res = cursor['m']+cursor['f']
        
        if res==m and facs==f:
            return(1)
        if res==f and macs==m:
        elif res > f:
            return(1)
            if memo.get(res,f)
            return float('inf')
        elif res > m:

        leftnode=cycle({'m':res,'f':facs},m,f)
        rightnode=cycle({'m':macs,'f':res},m,f)
        return 1+min(leftnode,rightnode)

    mach=int(m)
    facula=int(f)
    root={'m':1,'f':1}
    result=(cycle(root,mach,facula))
    if result == float('inf'):
        return 'impossible'
    return str(result)

# passing test 1 and 2