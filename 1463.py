N = int(input())

cnt_lst=[0,0,1]
cnt=0
for num in range(3,N+1):
    if num%6==0:
        cnt_lst.append(min(cnt_lst[num//3], cnt_lst[num//2]) + 1)
    elif num%3==0:
        cnt_lst.append(min(cnt_lst[num//3], cnt_lst[num-1]) + 1)
    elif num%2==0:
        cnt_lst.append(min(cnt_lst[num//2], cnt_lst[num-1]) + 1)
    else:
        cnt_lst.append(cnt_lst[num-1] + 1)
print(cnt_lst[N])