def solution(m,f):
    mach=int(m)
    facula=int(f)
    if abs(mach-facula)%2==0:
        return 'impossible'
    i=0
    while mach > 1 or facula > 1:
        i+=1
        if mach > facula:
            mach=mach-facula
        else:
            facula=facula-mach
    
    if mach==1 and facula==1:
        return str(i)
    
    return 'impossible'
    

print(solution('2','1'))
print(solution('4','7'))

# passing test 1 2 and 5