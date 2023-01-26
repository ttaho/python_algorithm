def n_queen(layer):
    global cnt
    if layer == N:
        cnt+=1
        return
    for i in range(N):
        if right_diagonal[layer+i] == 0 and left_diagonal[layer-i] == 0 and horizon[i] == 0:
            right_diagonal[layer+i], left_diagonal[layer-i], horizon[i] = 1, 1, 1
            n_queen(layer+1)
            right_diagonal[layer+i], left_diagonal[layer-i], horizon[i] = 0, 0, 0

N = int(input())
cnt=0
right_diagonal=[0 for _ in range(2*N-1)]
#-인덱스 +인덱스 다 사용
left_diagonal=[0 for _ in range(2*N-1)]
#해당 열못씀
horizon=[0 for _ in range(N)]

n_queen(0)
print(cnt)