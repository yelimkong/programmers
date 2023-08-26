def solution(num, total):
    avg = total // num
    
    return [n for n in range(avg - (num-1)//2, avg + (num+2)//2)]