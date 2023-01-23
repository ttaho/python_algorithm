from collections import deque
max_floor,start,end,up,down = map(int, input().split())
visited=[-1]*(max_floor+1)
visited[start]=0
movable=deque()
movable.append(start)
while movable:
    now = movable.popleft()
    if now == end:
        break
    if 1<= now+up <= max_floor and visited[now+up]==-1:
        movable.append(now+up)
        visited[now + up]=visited[now]+1
    if 1<= now-down <= max_floor and visited[now-down]==-1:
        movable.append(now-down)
        visited[now - down] = visited[now] + 1
if visited[end]==-1:
    print("use the stairs")
else:
    print(visited[end])

