def solution(my_string):
    numbers = [] # 자연수 저장 리스트 
    for char in my_string:
        if char.isdigit(): # 문자열이 숫자인 경우 
            numbers.append(int(char)) # 숫자를 자연수로 반환한 후 리스트 추가 
    return sum(numbers) # 자연수들의 합 반환 