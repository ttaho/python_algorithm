from collections import deque
def bfs(start_L,start_R,start_C):
    queue = deque()
    queue.append([start_L, start_R, start_C])
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            temp_x = x + move_x[i]
            temp_y = y + move_y[i]
            temp_z = z + move_z[i]
            if temp_x >= L or temp_x < 0 or temp_y >= R or temp_y < 0 or temp_z >= C or temp_z < 0:
                continue
            if buildings[temp_x][temp_y][temp_z] == 'E':
                print(f"Escaped in {minutes[x][y][z] + 1} minute(s).")
                return
            if buildings[temp_x][temp_y][temp_z] == '.' and minutes[temp_x][temp_y][temp_z] == 0:
                queue.append([temp_x, temp_y, temp_z])
                minutes[temp_x][temp_y][temp_z] = minutes[x][y][z] + 1
    print(f"Trapped!")
    return
move_x=[-1,0,0,1,0,0]
move_y=[0,-1,0,0,1,0]
move_z=[0,0,-1,0,0,1]

while True:
    L, R, C = map(int,input().split())
    if L==0 and R==0 and C==0:
        break
    buildings = []
    for _ in range(L):
        temp = []
        for _ in range(R):
            temp.append(list(map(str, input())))
        input()  # 층 구분
        buildings.append(temp)
    for_exit = False
    minutes = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)] #시간저장 3차원 배열
    #출발점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if buildings[i][j][k] == 'S':
                    start_L, start_R, start_C = i, j, k
                    for_exit = True
                    break
            if for_exit:
                break
        if for_exit:
            break
    bfs(start_L, start_R, start_C)
