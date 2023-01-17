import sys
#재귀 깊어지면 반드시 써야함!
sys.setrecursionlimit(10000)
def dfs(x,y):
    if x >= M or x < 0 or y >= N or y < 0:
        return False
    if map1[y][x] == 1:
        map1[y][x] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    warm=0
    M,N,K = map(int,input().split())
    map1=[[0 for _ in range(M)]for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        map1[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if dfs(j,i) == True:
                warm+=1
    print(warm)
