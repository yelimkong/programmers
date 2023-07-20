def solution(my_string, n):
    answer = []
    for st in my_string :
        answer.append(st * n) 
    return ''.join(answer)