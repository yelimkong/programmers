def solution(dots):
    
    max_x = max([i[0] for i in dots])
    min_x = min([i[0] for i in dots])
    
    max_y = max([i[1] for i in dots])
    min_y = min([i[1] for i in dots])
    
    return (max_x - min_x) * (max_y - min_y)
