def solution(N, number):
    if N == number:
        return 1  # N과 number가 같다면 바로 1 반환

    # dp[i]는 i개의 N을 사용하여 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN, ...

    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i  # number를 만드는데 필요한 최소 N의 개수

    return -1  # 8개 이내로 만들 수 없는 경우