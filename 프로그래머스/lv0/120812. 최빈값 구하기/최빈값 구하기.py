def solution(array):
    cnt = {} # 딕셔너리 생성

    for num in array: # array의 모든 원소를 돌면서
        if num not in cnt: # 해당 원소가 cnt 존재하지 않다면,
            cnt[num] = 0 # cnt에 새로 추가하고 value는 0으로 초기 설정
        cnt[num] += 1 # 이미 count에 존재하는 원소라면 value를 1 증가

    max_val = 0

    for k, v in cnt.items(): # .items()를 통해 key, value 쌍을 얻을 수 있음.
        if v > max_val: # 가장 큰 value 찾기
            max_val = v

    max_cnt = [k for k, v in cnt.items() if v == max_val] # 가장 큰 value일 경우의 key 즉 최빈값 k를 max_cnt 배열에 넣기
    if len(max_cnt) > 1: # 최빈값이 1개 이상일 경우 즉 위에서 max_cnt 배열에 여러 개의 key가 저장되었을 경우
        return -1
    else:
        return max_cnt[0]