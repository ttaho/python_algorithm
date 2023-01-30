N = int(input())
dp=[[0 for _ in range(10)]for _ in range(101)]
# 1자리수 세팅
for i in range(1,10):
    dp[1][i] = 1
#두자리 수 부터 만들기
for i in range(2,N+1):
    for j in range(0,10):
        #끝이 0이면 1에 추가
        if j == 0:
            dp[i][1] += dp[i-1][j]
        #끝이 9이면 8에 추가
        elif j == 9:
            dp[i][8] += dp[i-1][j]
        #나머지는 -1,+1에 추가
        else:
            dp[i][j-1] += dp[i-1][j]
            dp[i][j+1] += dp[i-1][j]

print(sum(dp[N]) % 1000000000)
