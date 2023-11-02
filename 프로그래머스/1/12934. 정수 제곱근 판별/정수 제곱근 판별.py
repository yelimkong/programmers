import math
def solution(n):
    answer = 0
    if math.sqrt(n)  == int(n**0.5) :
        return math.pow((math.sqrt(n) + 1), 2)
    else : 
        return -1
