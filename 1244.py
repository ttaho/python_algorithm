total = int(input())
arr = list(map(int,input().split()))
student = int(input())

for _ in range(student):
    sex, center = map(int,input().split())
    if sex == 1:
        for i in range(center-1,total,center):
            arr[i] = not arr[i]
    else:
        cnt=1
        new = min(center,total-center+1) #대칭확인할 범위지정
        for i in range(1,new):
            if arr[center-1-i] != arr[center-1+i]:
                break
            else:
                cnt+=1
        arr[center-1] = not arr[center-1]
        for i in range(1,cnt):
            arr[center-1-i], arr[center-1+i] = not arr[center-1-i], not arr[center-1+i]
for i in range(total):
    if arr[i] == True:
        arr[i] = 1
    elif arr[i] == False:
        arr[i] = 0
    print(arr[i],end=' ')
    if not (i+1)%20:
        print()