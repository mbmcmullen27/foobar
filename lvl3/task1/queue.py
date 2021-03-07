import math
import time 

def solution(n):
    pellets=int(n)
    if pellets <= 1: return 0
    queue=[{'ops':0,'count':pellets}]
    while len(queue)>0:
        time.sleep(1)
        print('\n{}'.format(queue))
        item=queue.pop(0)
        print('\n{}'.format(item))

        ops=item['ops']
        count=item['count']

        log=math.log(float(count),2)
        if  log==int(log) :
            return ops+int(log)

        if item['count'] == 1: 
            return item['ops']


        if count%2 == 0 :
            queue.append({'ops':ops+1,'count':count/2})
        if count < int('9'*309) :
            queue.append({'ops':ops+1,'count':count+1})
        
        queue.append({'ops':ops+1,'count':count-1})

print(solution('15'))
print(solution('4'))
print(solution('300'))
print(solution('9'*10))