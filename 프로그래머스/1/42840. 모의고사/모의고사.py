def solution(answers):
    # 수포자 학생 
    stu = [[1, 2, 3, 4, 5],  # 1번 
           [2, 1, 2, 3, 2, 4, 2, 5], # 2번
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번
          ]
    
    # 수포자 정답 개수
    ans = []
    for i in range(len(stu)):
        count = 0
        for j in range(len(answers)) :
            if answers[j] == stu[i][j % len(stu[i])]:
                count += 1
        ans.append(count)
        
    # 가장 높은 점수 받은 수포자
    result = []
    for j in range(len(ans)) :
        if ans[j] == max(ans):
            result.append(j + 1)
            
    return result

