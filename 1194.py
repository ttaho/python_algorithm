from collections import deque
N, M = map(int,input().split())
maze=[list(map(str,input()))for _ in range(N)]
out=False #시작값 찾기위한 boolean 변수
# 기존의 bfs는 2차원으로 visited를 만들어서 재방문을 못하게했지만,
# 해당문제는 가지고있는 key에 따라 재방문이 가능하므로 key상태인 1가지 차원을 추가하여 3차원으로 visited를 만든다.
visited=[[[0]*64 for _ in range(M)] for _ in range(N)]

#시작점 찾기
for i in range(N):
    for j in range(M):
        if maze[i][j] == "0":
            start_x,start_y = i,j
            maze[i][j] = '.'
            out=True
            break
    if out:
        break

def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y,0,0]) # x,y,cnt,keys(bit)
    visited[start_x][start_y][0] = 1
    move=[[0,1],[0,-1],[1,0],[-1,0]]
    while queue:
        now_x,now_y,cnt,keys = queue.popleft()
        # 도착점이면 return
        if maze[now_x][now_y] == '1':
            return cnt
        for temp_x,temp_y in move:
            x,y = now_x+temp_x, now_y+temp_y
            # 범위확인
            if x<0 or y<0 or x>=N or y>=M:
                continue
            # 해당키를 가지고 그곳에 방문하지 않은곳이어야함. 즉, 키변화없이 재방문 허용X
            if visited[x][y][keys]:
                continue
            if maze[x][y] == '.':
                queue.append([x,y,cnt+1,keys])
                visited[x][y][keys]=1

            elif maze[x][y].isalpha():
                # key 발견
                if maze[x][y].islower():
                    #해당 key로 keys 업데이트
                    new_keys = keys | (1<<ord(maze[x][y]) - 97)
                    #해당 key를 먹은적이 없으면 방문처리하고 keys 갱신, 해당 key를 먹은적 있으면 방문할 필요가 없음.
                    if visited[x][y][new_keys] == 0:
                        visited[x][y][new_keys] = 1
                        queue.append([x, y, cnt+1, new_keys])

                # 문 발견
                elif maze[x][y].isupper():
                    if keys & (1<<ord(maze[x][y]) - 65): # &연산은 둘다 1인것만 1 그러므로 해당문의 키를 가지고있으면
                        visited[x][y][keys] = 1
                        queue.append([x, y, cnt + 1, keys])

            elif maze[x][y] == '1':
                queue.append([x, y, cnt + 1, keys])
                visited[x][y][keys] = 1
    return -1
print(bfs(start_x,start_y))