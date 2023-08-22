def solution(quiz):
    answer = []
    for i in quiz :
        q = i.split('=')
        if eval(q[0]) == int(q[1]) :
            answer.append('O')
        else :
            answer.append('X')
        
    return answer
        
        
            