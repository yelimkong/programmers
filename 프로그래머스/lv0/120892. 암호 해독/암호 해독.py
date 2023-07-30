def solution(cipher, code):
    answer = ''
    # cipher의 길이 반환
    for c in range(code, len(cipher) +1): 
        
        # cipher 에서 code의 배수만 answer에 차례로 저장 
        if (c % code == 0) :
            answer += cipher[c - 1] 
    return answer