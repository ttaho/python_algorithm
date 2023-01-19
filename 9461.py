T = int(input())

for _ in range(T):
    length = [0, 1, 1, 1, 2, 2]
    N = int(input())
    for i in range(6,N+1):
        length.append(length[i-5]+length[i-1])
    print(length[N])