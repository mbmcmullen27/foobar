def solution(m,f):
    mach=int(m)
    facula=int(f)
    root={'m':1,'f':1, 'depth':0}
    result=(cycle(root,mach,facula))
    if result == float('inf'):
        return 'impossible'
    return str(result)

memo=dict()
def cycle(cursor,m,f):

    macs=cursor['m']
    facs=cursor['f']
    ops=cursor['depth']

    res = cursor['m']+cursor['f']

    if macs==m and facs==f:
        print('({},{}) -> m:{} f:{} res = {}'.format(m,f,macs,facs,res))
        return ops
    elif facs > f or macs > m:
        return float('inf')

    left={'m':res,'f':facs, 'depth':ops+1}
    right={'m':macs,'f':res, 'depth':ops+1}
    
    key=(res,facs)
    if not memo.get(key) or memo[key]>ops+1: 
        memo[key] = cycle(left,m,f)
    genleft=memo[key]

    key=(macs,res)
    if not memo.get(key) or memo[key]>ops+1:
        memo[key] = cycle(right,m,f)
    genright=memo[key]

    return min(genleft,genright)


print('final solution: {}'.format(solution('2','1')))
print('final solution: {}'.format(solution('4','7')))

# passes 1 and 2