INF = int(1e9) # 무한을 의미하는 값 , 10억 설정

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수 

cost = [[INF] * (n +1) for _ in range(n + 1)] # 

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1, n +1):
    for b in range(1, n +1) :
        if a == b:
            cost [a][b] = 0 
            
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화 
for _ in range(m) :
    # a : 버스의 시작 도시, b : 버스의 도착 도시, c : 비용 
    a, b, c = map(int, input().split())
    # A에서 B로 가는 비용은 C, 가장 적은 비용 저장
    if c < cost[a][b] :
        cost[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행 
for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
            
# 수행된 결과를 출력 
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        #도달할 수 없는 경우, 무한이라고 출력 
        if cost[i][j] == INF :
            print(0, end = " ")
        # 도달할 수 있는 경우 거리를 출력 
        else : 
            print(cost[i][j], end = " ")
    print()