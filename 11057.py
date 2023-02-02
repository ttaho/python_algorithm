N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        temp_sum=0
        for k in range(0,j+1):
            temp_sum+=dp[i-1][k]
        dp[i][j] = temp_sum

print(sum(dp[N]) % 10007)