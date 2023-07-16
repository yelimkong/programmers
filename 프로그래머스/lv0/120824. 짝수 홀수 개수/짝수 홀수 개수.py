def solution(num_list):
    answer = []
    
    a, b = 0, 0
    
    for n in num_list :
        if n % 2 == 0 :
            a += 1
        else :
            b += 1
            
    answer = [a, b]
            
    return answer
          
