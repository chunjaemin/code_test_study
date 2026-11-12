def solution(park, routes):
    N = len(park)
    M = len(park[0]) 
    D = {
        'E' : 0,
        'W' : 1,
        'S' : 2,
        'N' : 3
    }
    X = [0,0,1,-1]
    Y = [1,-1,0,0]
    
    x = 0
    y = 0 
    for r in range(N):
        for c in range(M):
            if park[r][c] == 'S':
                x = r
                y = c 
    for s in routes:
        d, a = s.split(" ")
        n = int(a)
        nx = x + X[D[d]] * n
        ny = y + Y[D[d]] * n
        if 0 <= nx < N and 0<= ny < M:
            check = 1 
            for i in range(1,n+1):
                if park[x+X[D[d]]*i][y+Y[D[d]]*i] == 'X':
                    check = 0 
            if check:
                x = nx 
                y = ny 
    
    answer = [x,y]
    return answer