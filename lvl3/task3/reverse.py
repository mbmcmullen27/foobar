def solution(m,f):
    mach=int(m)
    facula=int(f)

    i=0
    while mach > 1 and facula > 1:
        print('({},{}) -> m:{} f:{}'.format(m,f,mach,facula))
        if mach==facula:
            break
        i+=1
        if mach > facula:
            scalar=max(mach/facula,1)
            mach=mach-(scalar*facula)
            print('scalar: {} mach: {} facula: {}'.format(scalar,mach,facula))
        else:
            scalar=max(facula/mach,1)
            facula=facula-(scalar*mach)
    
    if mach==1 and facula>1:
        return str(i+facula-1)
    
    if mach>1 and facula==1:
        return str(i+mach-1)

    return 'impossible'
    

print(solution('2','1'))
print(solution('4','7'))
print(solution('5'*10,'78765'*3))

# passing test 1 2 and 5