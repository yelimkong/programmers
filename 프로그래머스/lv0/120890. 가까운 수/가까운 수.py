def solution(array, n):
    result = [] 
    array.sort()
    for i in array :
        result.append(abs(n-i))
    answer = [array[result.index(min(result))]]
    if len(answer) > 1:
        return min(answer)
    else :
        return answer[0]
