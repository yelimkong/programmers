import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 리스트를 힙으로 변환
    answer = 0
    
    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
    while scoville[0] < K:  
        if len(scoville) > 1:
            f = heapq.heappop(scoville)  # 가장 작은 지수
            s = heapq.heappop(scoville)  # 두 번째로 작은 지수  
            mix = f + 2 * s  #  지수 계산
            
            heapq.heappush(scoville, mix)  # 힙에 새 스코빌 지수 삽입
            answer += 1  # 섞은 횟수 증가
        else:
            return -1 

    return answer

