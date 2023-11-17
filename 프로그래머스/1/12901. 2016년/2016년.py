def solution(a, b):
    answer = ''
    weekday = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE', 'WED']
    # 윤년 : 2월 29일까지 있는 해
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = b
    for i in range(a) :
        day += month[i]
    day %= 7
    answer = weekday[day]
    return answer