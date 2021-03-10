def solution(m,f):
    mach=int(m)
    facula=int(f)

    i=0
    while mach > 1 and facula > 1:
        if mach==facula:
            break
        scalar=None
        if mach > facula:
            scalar=max(mach/facula,1)
            mach=mach-(scalar*facula)
        else:
            scalar=max(facula/mach,1)
            facula=facula-(scalar*mach)
        i+=scalar
    
    if mach==1 and facula>1:
        return str(i+facula-1)
    
    if mach>1 and facula==1:
        return str(i+mach-1)

    return 'impossible'
    


# all tests passed!