
N = int(input())
n = len(str(N))

array = [int(i) for i in str(N)]         # N을 문자로 쪼개서 리스트에 각 자리수 별 다시 저장 

start = 0                                 # 첫 번째 인덱스
end = len(array) - 1                      # 마지막 인덱스


def lucky(array, start, end):             
    mid = (start + end) // 2              # 중간 인덱스
    
    # array의 0 ~ 중간 인덱스 까지 더한 값과 중간 + 1 ~ 마지막 인덱스까지 더한 값이 같다면
    if sum(array[start:mid + 1]) == sum(array[mid + 1:end + 1]):
        return "LUCKY"                    # LUCKY 반환
    else:                                 # 같지 않다면
        return "READY"                    # READY 반환

result = lucky(array, start, end)         # 결과 값



print(result)
