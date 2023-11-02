import math

def solution(n):
    answer = 0
    if math.sqrt(n)  == int(n**0.5) : # n의 제곱근이 n에 루트 씌운 것과 같다면
        return math.pow((math.sqrt(n) + 1), 2) # n의 제곱근 + 1을 제곱하고
    else : # 제곱근이 존재하지 않는다면
        return -1 # -1을 반환
