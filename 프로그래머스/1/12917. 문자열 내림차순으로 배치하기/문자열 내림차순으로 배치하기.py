def solution(s):
    up = []  # 대문자 저장
    low = []  # 소문자 저장

    # 대소문자를 구분하여 리스트에 추가
    for char in s:
        if char.isupper():
            up.append(char)
        else:
            low.append(char)

    # 리스트를 정렬 (대문자 우선, 알파벳 순)
    up.sort(reverse=True)
    low.sort(reverse=True)

    # 정렬된 대문자와 소문자를 합쳐서 반환
    answer = ''.join(low + up)

    return answer
