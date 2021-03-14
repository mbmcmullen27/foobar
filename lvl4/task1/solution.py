def solution(banana_list):
    if len(banana_list) == 1: return 1
    for i in banana_list:
        root=banana_list.pop(i)
        pool=banana_list[:]
        while pool:
            challenger=pool.pop(0)
            res=play(challenger,root)


    return 'glub...'

def play(player1,player2):
    

print(solution('test'))