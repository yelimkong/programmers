def solution(arr1, arr2):
    answer = []
    # 전체 배열 길이
    for i in range(len(arr1)) :
        answer_sum = []
        # 배열 한 행 길이
        for j in range(len(arr1[0])) :
            answer_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_sum)
    return answer
        