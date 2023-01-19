import sys
N, M = map(int,sys.stdin.readline().split())
pocketmon={}
for i in range(1,N+1):
    pocketmon[sys.stdin.readline().rstrip()]=i
reverse_pocketmon = dict(map(reversed,pocketmon.items()))
for _ in range(M):
    answer = sys.stdin.readline().rstrip()
    if answer.isdigit():
        print(reverse_pocketmon[int(answer)])
    else:
        print(pocketmon[answer])