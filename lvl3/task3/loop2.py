def solution(m,f):
    mach=int(m)
    facula=int(f)
    root={'m':1,'f':1}
    result=(cycle(root,mach,facula))
    if result == float('inf'):
        return 'impossible'
    return str(result)

def cycle(cursor,m,f):

    macs=cursor['m']
    facs=cursor['f']

    res = cursor['m']+cursor['f']
    
    print('({},{}) -> m:{} f:{} res = {}'.format(m,f,macs,facs,res))
    if res==m and facs==f:
        return(1)
    if res==f and macs==m:
        return(1)
    elif res > f or res > m:
        print('{} {} returning infinity'.format(macs,facs))
        return float('inf')

    leftnode=cycle({'m':res,'f':facs},m,f)
    rightnode=cycle({'m':macs,'f':res},m,f)
    print(leftnode)
    print(rightnode)
    return 1+min(leftnode,rightnode)

print('final solution: {}'.format(solution('2','1')))
print('final solution: {}'.format(solution('4','7')))

# passing test 1 and 2