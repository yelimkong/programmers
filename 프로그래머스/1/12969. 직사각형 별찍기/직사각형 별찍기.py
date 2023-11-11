# 사용자로부터 입력 받기
n, m = map(int, input().split())

def solution(n,m) :
    for _ in range(m):
        print('*' * n)
        
solution(n,m)
        
