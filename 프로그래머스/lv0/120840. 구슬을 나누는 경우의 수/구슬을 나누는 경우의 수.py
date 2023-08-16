from math import factorial as fac

def solution(balls, share):
    answer = 0
    a = fac(balls)
    b = fac(share)
    botton = fac(balls - share) * b 
    return a / botton