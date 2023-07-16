def solution(str1, str2):
    answer = 0
    
    for str in str1 :
        if str2 in str1 :
            return 1
        else :
            return 2
    
    
