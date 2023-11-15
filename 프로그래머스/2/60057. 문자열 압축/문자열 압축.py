
def solution(s):
    answer = len(s)  # 초기값은 문자열 길이로 설정

    for length in range(1, len(s) // 2 + 1):  # 문자열 압축 단위 개수 확인
        str_c = []  # 초기화
        for i in range(0, len(s), length):  # 문자열을 최대 압축 단위만큼 쪼개기
            substr = s[i:i + length]  # 범위만큼 쪼갠 문자열 substr 변수에 저장

            if str_c and str_c[-1][0] == substr:  # 직전에 저장한 문자열과 현재 문자열이 같다면
                str_c[-1] = (substr, str_c[-1][1] + 1)  # 튜플의 원소의 값 + 1 증가
            else:  # 같지 않다면 (처음은 초기화 상태라 else 부터 시작)
                str_c.append((substr, 1))  # 새로운 튜플을 추가

        # 결과를 문자열로 합치기
        result_str = []

        for substr, count in str_c:  # 튜플의 값을 문자와 숫자로 나눈다.
            if count > 1:  # 숫자가 1보다 크면
                result_str.append(str(count) + substr)  # ex) ('a', 2) 이 구조에서 2a로
            else:
                result_str.append(substr)  # 숫자가 1보다 작다면 그대로 문자만 반환

        result_str = ''.join(result_str)  # 하나의 문자열로 연결

        # 결과의 길이 계산 및 저장
        result_length = len(result_str)
        answer = min(answer, result_length)  # 최소값 갱신

    return answer  # 결과값을 반환
