def solution(num, k):
    answer = -1
    a = str(num)
    for i in range(len(a)):
        if int(a[i]) == k:
            return i+1
    return answer
 