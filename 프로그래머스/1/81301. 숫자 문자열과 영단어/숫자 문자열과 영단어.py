def solution(s):
    answer= s
    words = {'zero' : '0',
            'one' : '1', 
            'two' : '2', 
            'three' : '3', 
            'four' : '4', 
            'five' : '5', 
            'six' : '6', 
            'seven' : '7', 
            'eight' : '8', 
            'nine' : '9'}
    
    for w, i in words.items() :
        answer = answer.replace(w, i)
        
    return int(answer)