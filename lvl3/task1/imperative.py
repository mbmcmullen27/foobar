import time

def solution(n):
    pellets=int(n)
    return sift(pellets)
    
def sift(pellets):
    if pellets == 1: return 0
    queue=[{'ops':1,'count':pellets}]
    while len(queue)>0:
        # time.sleep(1)
        print('\n{}'.format(queue))
        item=queue.pop(0)
        print('\n{}'.format(item))

        if item['count'] == 1: 
            return item['ops']

        ops=item['ops']
        count=item['count']
        if count%2 == 0 :
            queue.append({'ops':ops+1,'count':count/2})
        else:        
            queue.append({'ops':ops+1,'count':count+1})
            queue.append({'ops':ops+1,'count':count-1})


# print solution('9'*309)
# print solution('300')

print(solution('15'*30))
print solution('4')
print solution('15')