def solution(n):
    result = varieties(n)
    print result
    return len(result)

def varieties(n):
    if n == 3:
        return [(2,1)]
    if n == 4:
        return [(3,1)]
    elif n <= 200:
        steps = varieties(n-1)
        result=set()
        for variant in steps :
            variant=list(variant)
            i=0
            while i < len(variant) :
                # print variant
                before=None
                after=None

                if i == 0 : 
                    before = float('inf')
                else:
                    before = variant[i-1]

                if i == len(variant)-1: 
                    after = 0
                    if variant[i] > 1 : 
                        extension=variant[0:]
                        extension.append(1)
                        # print('extension {} - i:{}'.format(variant,i))
                        result.add(tuple(extension))
                        # print extension
                else:
                    after = variant[i+1]

                if variant[i]+1 < before and variant[i]+1 > after:
                    prefix=list(variant[0:i])
                    index=[variant[i]+1]
                    postfix=list(variant[i+1:])
                    product=prefix+index+postfix
                    result.add(tuple(product))
                    # print product
               
                i+=1
        return result

print solution(3)
print solution(4)
# print solution(200)
print solution(5)
print solution(6)
print solution(7)
print solution(8)
print solution(9)
print solution(10)
print solution(11)
print solution(12)