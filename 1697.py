from collections import deque
N, K = map(int,input().split())
check=[-1]*100001
check[N]=0
queue= deque()
queue.append(N)
while queue:
    now = queue.popleft()
    if now == K:
        break
    for i in(now-1,now+1,now*2):
        if 0<=i<=100000 and check[i] == -1:
            check[i] = check[now]+1
            queue.append(i)
print(check[K])