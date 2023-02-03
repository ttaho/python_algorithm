import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visit=[0]*(N+1)
cnt=0
def bfs():
    global cnt
    q = deque()
    for j in range(1,N+1):
        if visit[j]==0:
            visit[j]=1
            q.append(j)
            while q:
                now = q.popleft()
                for i in range(1,N+1):
                    if visit[i] == 0 and i in graph[now]:
                        q.append(i)
                        visit[i] =1
            cnt+=1
    return cnt
print(bfs())