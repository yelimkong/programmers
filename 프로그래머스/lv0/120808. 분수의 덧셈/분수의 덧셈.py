import math

def solution(numer1, denom1, numer2, denom2):
    # 1. 두 분수의 합 계산 
    bj = numer1*denom2 + denom1*numer2
    bm = denom1*denom2
    
    # 2. 최대 공약수 계산
    gcd_value = math.gcd(bj, bm)
    
    # gcd 로 나눈 값을 answer 에 담기
    answer = [bj / gcd_value, bm / gcd_value]
    return answer