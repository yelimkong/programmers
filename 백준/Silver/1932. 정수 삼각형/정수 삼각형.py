# 삼각형의 크기 
n = int(input()) 

# 정수 삼각형
tri = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * n for _ in range(n)]
dp[0][0] = tri[0][0]  # 첫 번째 줄의 값은 초기값

# 삼각형의 줄 
for i in range(1, n):
    # i번째 줄의 위치 
    for j in range(i + 1):
        # 왼쪽 대각선 위에서 내려옴 (위치가 두번째부터 일 때 )
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + tri[i][j])
        # 오른쪽 대각선 위에서 내려옴
        if j < i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + tri[i][j])

# 마지막 줄에서 최대값 찾기
# n-1 한 이유 : 인덱스가 0부터 시작하니까 
result = max(dp[n - 1])

print(result)  