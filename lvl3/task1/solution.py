#Dijkstra's 

import math

def solution(n):
    pellets=int(n)
    d=dict()
    d[n]=0
    queue=[{'ops':0,'count':pellets}]
    while len(queue)>0:
        item=queue.pop(0)
        ops=item['ops']
        count=item['count']

        if count == 1: 
            return ops  

        record=d.get(str(count))
        if not record: 
            d[str(count)] = ops
            record = d[str(count)]

        if ops <= record:
            if count%2 == 0 :
                key=str(count/2)
                if not d.get(key): d[key] = float('inf')
                
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
