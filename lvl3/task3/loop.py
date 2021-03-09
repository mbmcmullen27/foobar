def solution(m,f):
    mach=int(m)
    facula=int(f)
    root={'m':1,'f':1}
    result=(cycle(root,mach,facula))
    # print('result: {}'.format(result))
    if result == float('inf'):
        return 'impossible'
    return str(result)

def cycle(cursor,m,f):
    print cursor
    macs=cursor['m']
    facs=cursor['f']

    res = cursor['m']+cursor['f']
    print('m:{} f:{} cur = {}'.format(macs,facs,cursor))
    if res==m and facs==f:
        print('m:{} f:{} res = {}'.format(macs,facs,res))
        return(1)
    if res==f and macs==m:
        print('m:{} f:{} res = {}'.format(macs,facs,res))
        return(1)

    if res > m and res > f:
        return float('inf')
    else:
        leftnode=1+cycle({'m':res,'f':f},m,f)
        rightnode=1+cycle({'m':m,'f':res},m,f)

    return min(leftnode,rightnode)



print(solution('2','1'))
print(solution('4','7'))

# passing test 2 and 4