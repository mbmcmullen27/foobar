def solution(m,f):
    mach=int(m)
    facula=int(f)
    root={'count':0,'m':1,'f':1}
    return cycle(root,mach,facula)

def cycle(cursor,m,f):
    count=cursor['count']
    macs=cursor['m']
    facs=cursor['f']

    res = int(m)+int(f)

    if res > m or res > f:
        return float('inf')
    
    if macs+res==m and facs==f:
        return cursor['count']
    if facs+res==f and macs==m:
        return cursor['count']
    
    leftnode=cycle({'count':count+1,'m':res,'f':f},m,f)
    rightnode=cycle({'count':count+1,'m':m,'f':res},m,f)

    return min(leftnode,rightnode)



print(solution('2','1'))
print(solution('4','7'))