def solution(m,f):
    mach=int(m)
    facula=int(f)
    return min(solution(mach,facula))

print(solution('2','1'))
print(solution('4','7'))