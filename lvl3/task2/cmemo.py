def solution(n):
    memo = dict()
    cap = dict()
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
                k+=1
            

            for i in range(k,n-1):
                j=n-i-1
                index=i-j
                if not cap.get(j): cap[j] = capacity(j)
                if(cap[j]+(n-i)>n):
                    print('--> ({},{})'.format(i,index))
                    sets+=varieties(i,index)

            # while k<n-1:
            #     print('--> calling ({},{}) sets: {}'.format(k,k-index,sets))
            #     k+=1

            # print('{}: ({},{}) sets: {}'.format(n,n-k,k,sets))
            return sets


    return varieties(n,1)

def capacity(n):
    sum=0
    for i in range(1,n+1):
            sum += i
            i+=1
    return sum


# print(solution(200))
# print ('\nSets Possible: {}'.format(solution(9)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(10)))
# print ('\n***************************')
# print ('\nSets Possible: {}'.format(solution(11)))
# print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(12)))
print ('\n***************************')
print ('\nSets Possible: {}'.format(solution(13)))
# print ('\nSets Possible: {}'.format(solution(20)))