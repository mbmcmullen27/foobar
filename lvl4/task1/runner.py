import random
import flip_matches as subject

def randomset(length):
    res=[]
    for i in range(length):
        res.append(random.randrange(2**20 - 1))
    print res
    return res


# print simple_symmetry.solution([1,7,3,21,13,19])
banana_list=randomset(20)
print subject.solution(banana_list)
print banana_list

# I think the history/memoizing of the matchlist method is running long