
import math 

def solution(n):
    pellets=int(n)
    if pellets <= 1: return 0
    queue=[{'ops':0,'count':pellets}]
    while len(queue)>0:

        item=queue.pop(0)

        ops=item['ops']
        count=item['count']

        if count == 1: 
            return ops

        # if count and not (count & (count - 1)):
        #     return ops+int(math.log(count,2));  

        if count%2 == 0 :
            queue.append({'ops':ops+1,'count':count/2})

        if count < int('9'*309) :
            queue.append({'ops':ops+1,'count':count+1})
        
        queue.append({'ops':ops+1,'count':count-1})

print(solution('15'))
print(solution('4'))
print(solution('300'))
print(solution('9'*10))