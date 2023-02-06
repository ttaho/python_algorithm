N,K = map(int,input().split())
arr=[i for i in range(1,N+1)]
num=0
new_arr=[]
while arr:
    num+=K-1
    if num>=len(arr):
        num%=len(arr)
    new_arr.append(arr.pop(num))
print("<",end="")
for i in range(len(new_arr)-1):
    print(f'{new_arr[i]}, ',end="")
print(f'{new_arr[-1]}>')



# arr=[1,2,3,4,5]
# arr.pop(3)
# arr = arr[3:] + arr[:3]
# print(arr)