def solution(s):
    words = s.split(" ")  # 입력 문자열을 공백을 기준으로 단어로 분리
    
    result = []  # 수정된 단어들을 저장할 리스트를 초기화

    for index, word in enumerate(words):
        version = ''  # 현재 단어의 수정된 버전을 저장할 변수를 초기화

        # 단어의 각 문자에 대해 인덱스가 홀수이면 대문자로, 짝수이면 소문자로 변환
        for idx, char in enumerate(word):
            if idx == 0:
                version += char.upper()
            elif idx % 2 == 0:
                version += char.upper()
            else:
                version += char.lower()

        result.append(version)  # 수정된 단어를 리스트에 추가

        # 현재 단어가 마지막 단어가 아니면 공백을 추가
        if index < len(words) - 1:
            result.append(' ')

    return ''.join(result)  # 리스트 안의 단어들을 이어붙여 최종 문자열로 생성

    