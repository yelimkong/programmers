def solution(keyinput, board):
    limit_x = board[0]//2
    limit_y = board[1]//2
    start = [0,0]
    
    direction = {'up' : [0,1], 'down' : [0,-1],'left' : [-1,0], 'right' : [1,0]}
    for i in keyinput:
        dx, dy = direction[i]
        if abs(start[0] + dx)> limit_x or abs(start[1]+dy) >limit_y:
            continue
        else:
            start[0] += dx
            start[1] += dy
    return start