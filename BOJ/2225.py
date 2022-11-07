# dp[n][k] = 정수 k개를 더해서 합이 n이 되는 경우의 수
# dp[1][1] = 1 (1)
# dp[1][2] = 2 (0+1, 1+0)
# dp[1][3] = 3 (0+0+1, 0+1+0, 1+0+0)
# dp[1][4] = 4 (0+0+0+1, 0+0+1+0, 0+1+0+0, 1+0+0+0)

# dp[2][1] = 1 (2)
# dp[2][2] = 3 (0+2, 2+0, 1+1)
# dp[2][3] = 6 (0+0+2, 0+2+0, 2+0+0, 0+1+1, 1+0+1, 1+1+0)
# dp[2][4] = 10(0+0+0+2, 0+0+2+0, 0+2+0+0, 2+0+0+0,
#               0+0+1+1, 0+1+0+1, 0+1+1+0, 1+0+1+0, 1+1+0+0, 1+0+0+1)

# dp[3][1] = 1 (3)
# dp[3][2] = 4 (0+3, 3+0, 1+2, 2+1)
# dp[3][3] = (0+0+3, 0+3+0, 3+0+0, 1+1+1, 0
#             0+1+2, 0+2+1, 1+2+0, 1+0+2, 2+0+1, 2+1+0)


n, k = map(int, input().split())
mod = 1000000000
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n][k] % mod)
