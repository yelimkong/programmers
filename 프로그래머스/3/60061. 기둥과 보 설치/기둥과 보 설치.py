# 체크하는 함수
def check(answer) :
    for x, y, a in answer :
    # 구조물이 겹치도록 삭제하는 경우 
    # a = 1 보일 때 삭제하는 경우 한쪽 끝부분이 기둥 위거나 양쪽에 다른 보와 연결되어 있는 지 확인 
        if a == 1 :
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer) :
                continue 
            return False 

        # a = 0 기둥일 때
        elif a == 0 :
            # 바닥 위에 있거나 보의 한쪽 끝부분 위거나 다른 기둥 위인지 확인
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer :
                continue 
            return False 
    
    return True
    

def solution(n, build_frame):
    
    # x, y 좌표 담을 빈 리스트 
    answer = []
    
    for x, y, a, b in build_frame :

        # b가 0일 경우 삭제
        if b == 0 :
            answer.remove([x, y, a])
            if not check(answer) :
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a]) 
            if not check(answer) :
                answer.remove([x, y, a])
                
    return sorted(answer)
    