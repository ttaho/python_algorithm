N = int(input())
arr=[0]*300
dp=[0]*300
for i in range(N):
    arr[i] = int(input())
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2] = max(arr[1] + arr[2], arr[0] + arr[2])
for i in range(3,N):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
print(dp[N-1])