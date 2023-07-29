def solution(before, after):
    answer = 0
    result = ''
    for i in before :
        if before.count(i) == after.count(i):
            result += i 
    if len(result) == len(after) :
        answer = 1
    else : 
        answer = 0
        
    return answer