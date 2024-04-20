import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 리스트를 힙으로 변환
    answer = 0
    
    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
    while scoville[0] < K:  
        if len(scoville) > 1:
            first = heapq.heappop(scoville)  # 가장 작은 지수
            second = heapq.heappop(scoville)  # 두 번째로 작은 지수  
            new = first + 2 * second  #  지수 계산
            
            heapq.heappush(scoville, new)  # 힙에 새 스코빌 지수 삽입
            answer += 1  # 섞은 횟수 증가
        else:
            return -1  # 두 개 이상의 스코빌 지수가 없을 때 K 이상을 만들 수 없으므로 -1 반환

    return answer

