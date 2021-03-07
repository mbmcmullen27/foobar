import math
import time

def solution(n):
    pellets=int(n)
    # if pellets <= 1: return 0
    d=dict()
    d[n]=0
    queue=[{'ops':0,'count':pellets}]
    while len(queue)>0:
        # time.sleep(1)
        # print('\n{}'.format(d))
        print('{}'.format(queue))
        item=queue.pop(0)
        print('----> POP {}'.format(item))

        ops=item['ops']
        count=item['count']

        if count == 1: 
            return ops  

        record=d.get(str(count))
        if not record: 
            d[str(count)] = ops
            record = d[str(count)]

        # print record
        if ops <= record:
            if count%2 == 0 :
                key=str(count/2)
                if not d.get(key): d[key] = float('inf')
                
                # print('******{} < {}'.format(d[key],record))
                if record+1 < d[key] :
                    queue.append({'ops':ops+1,'count':count/2})
                    d[key] = ops+1
            else:
                key=str(count-1)
                if not d.get(key): d[key] = float('inf')

                if record+1 < d[key] :
                    queue.append({'ops':ops+1,'count':count-1})
                    d[key] = ops+1

                if count < int('9'*309) :
                    key=str(count+1)
                    if not d.get(key): d[key] = float('inf')

                    if record+1 < d[key] :
                        queue.append({'ops':ops+1,'count':count+1})
                        d[key] = ops+1          




# print(solution('15'))
# print(solution('4'))
# print(solution('300'))
print(solution('9'*10))

# if[^:]*$ 
# ifs missing colons