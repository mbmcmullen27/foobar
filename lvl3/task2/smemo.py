def solution(n):

    memo = dict()
    # cap = dict()
    def varieties(n,k):
        if n < 3: return 0
        if n <= 4: return 1
        elif n <= 200:
            
            sets=0
            while n-k>k:
                if not memo.get(k): memo[k] = varieties(k,1)
                sets+= (memo[k] + 1)
                print('{}: Main loop: ({},{}) sets: {}'.format(n,n-k,k,sets))
                k+=1
            
            if k==n-k:
                if not memo.get(k): memo[k] = varieties(k,1)
                sets+=(memo[k])
                print('Equals difference: n={} k={} n-k={}'.format(n,k,n-k))
                k+=1
            
            index=n-k-1
            print('{}: ({},{}) [{}] sets: {}'.format(n,n-k,k,index,sets))

            print('{}: Less than: k={} n-k={} ---> {}'.format(n,k,n-k,index))
            if((n-k)+index>k):
                sets+=varieties(k,k-index)
            print('{}: ({},{}) sets: {}'.format(n,n-k,k,sets))
            return sets

    return varieties(n,1)
def cap(n):
    sum=0
    for i in range(n):
        sum+=i
        i+=1
    return sum

# # print(solution(200))
# print ('\nSets Possible: {}'.format(solution(9)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(10)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(11)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(12)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(13)))
print ('\nSets Possible: {}'.format(solution(20)))