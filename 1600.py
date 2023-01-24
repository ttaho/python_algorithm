from collections import deque
K = int(input())
width, height = map(int, input().split())
#말처럼 이동하기
knight_yx=[[-1,-2],[-2,-1],[-2,1],[-1,2],[1,-2],[2,-1],[2,1],[1,2]]

#그냥 이동하기
common=[[0,1],[0,-1],[1,0],[-1,0]]
#visited[y좌표][x좌표][말처럼이동한횟수] = 총 이동거리
visited=[[[-1]*(K+1) for _ in range(width)] for _ in range(height)]
board=[list(map(int,input().split())) for _ in range(height)]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 0
    while queue:
        y, x, move_like_knight = queue.popleft()
        # 도착점이면 종료
        if y == height - 1 and x == width - 1:
            return visited[y][x][move_like_knight]
        # 일단 그냥이동하기
        for temp_y, temp_x in common:
            now_y, now_x = y + temp_y, x + temp_x
            # 보드범위 확인, 장애물이 없고, 방문하지 않은곳인 경우
            if 0 <= now_y < height and 0 <= now_x < width and board[now_y][now_x] == 0 and visited[now_y][now_x][move_like_knight] == -1:
                # 현재 총이동거리+1
                visited[now_y][now_x][move_like_knight] = visited[y][x][move_like_knight] + 1
                queue.append([now_y, now_x, move_like_knight])
        # 말처럼 이동하는 횟수 남아있는 경우
        if move_like_knight < K:
            for temp_y, temp_x in knight_yx:
                now_y, now_x = y + temp_y, x + temp_x
                # 보드의 범위 확인, 장애물이 없고, 방문하지 않은곳인 경우
                if 0 <= now_y < height and 0 <= now_x < width and board[now_y][now_x] == 0 and visited[now_y][now_x][move_like_knight + 1] == -1:
                    # 현재 총이동거리+1
                    visited[now_y][now_x][move_like_knight + 1] = visited[y][x][move_like_knight] + 1
                    queue.append([now_y, now_x, move_like_knight + 1])
    return -1

print(bfs())