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

    if macs==m and facs==f:
        print('({},{}) -> m:{} f:{} res = {}'.format(m,f,macs,facs,res))
        return(0)
    elif facs > f or macs > m:
        return float('inf')

    leftnode=cycle({'m':res,'f':facs},m,f)
    rightnode=cycle({'m':macs,'f':res},m,f)
    return 1+min(leftnode,rightnode)


print('final solution: {}'.format(solution('2','1')))
print('final solution: {}'.format(solution('4','7')))

# passes 1 and 2