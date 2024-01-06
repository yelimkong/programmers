n = int(input())
m = list(map(int, input().split()))

m.reverse()
dp = [1] * n


for i in range(1, n) :
    for j in range(0, i) :
        if m[j] < m[i] :
            dp[i] = max(dp[i], dp[j] + 1)
    
print(n - max(dp))