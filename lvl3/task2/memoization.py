def solution(n):
    print('{} BRICKS\n'.format(n))
    return varieties(n)

memo = dict()
def varieties(n):
    if n < 3: return 0
    if n <= 4: return 1
    elif n <= 200:
        
        sets=0
        k=1    
        while n-k>k:
            if not memo.get(k): memo[k] = varieties(k)
        
            sets+= (memo[k] + 1)
        
            print('{}: ({},{}) sets: {}'.format(n,n-k,k,sets))
            k+=1
        
        if not memo.get(k): memo[k] = varieties(k)
        # print('n={}:k={}'.format(k,memo[k]))
        if k==n-k:
            sets+=(memo[k])
            print('n==n-k n={} k={} n-k={}'.format(n,k,n-k))
        elif k>4:
            print('n!=n-k n={} k={} n-k={}'.format(n,k,n-k))
            sets+=(memo[n-k])
            # print('ne memo[{}]:{}'.format(k,memo[k]))
        print('{}: ({},{}) sets: {}'.format(n,n-k,k,sets))
        return sets

# print ('\nSets Possible: {}'.format(solution(3)))
# print ('\nSets Possible: {}'.format(solution(4)))
# print ('\nSets Possible: {}'.format(solution(200)))
# print ('\nSets Possible: {}'.format(solution(5)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(6)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(7)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(8)))
# print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(9)))
print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(10)))
print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(11)))
print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(12)))
print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(13)))
# print ('\nSets Possible: {}'.format(solution(20)))  