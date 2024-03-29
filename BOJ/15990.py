# dp[1] = 1 (1)
# dp[2] = 1 (2)
# dp[3] = 2 (1+2, 2+1, 3)
# dp[4] = 3 (1+2+1, 1+3, 3+1)
# dp[5] = 4 (2+3, 3+2, 2+1+2, 1+3+1)
# dp[6] = 6 (1+3+2, 1+2+3, 3+2+1, 3+1+2, 2+1+3, 2+3+1, 1+2+1+2, 2+1+2+1)
# dp[7] = 9
# => dp[n] = dp[n-1] + dp[n-3]

# 2차원 리스트로 생각해야함
# dp[1] = [1,0,0]
# dp[2] = [0,1,0]
# dp[3] = [1,1,1]
# => dp[4] = [2,0,1] (3에서 ~~1에 +2, ~~3에 +1 해주면 되니)
# dp[4][0] = dp[3][1] + dp[3][2]   (3+1)
# dp[4][1] = dp[2][0] + dp[2][2]   (2+1+1)
# dp[4][2] = dp[1][0] + dp[3][1]   (1+3)
# => dp[5] = [1,2,1]
# dp[5][0] = dp[4][1] + dp[4][2]
# dp[5][1] = dp[3][0] + dp[3][2]
# dp[5][2] = dp[2][0] + dp[3][1]
# => dp[6] = [2,2,2]
#       = dp[5][1] + dp[5][2]
#       = dp[4][0] + dp[4][2]
#       = dp[3][0] + dp[3][1]
import sys
input = sys.stdin.readline
t = int(input())

# dp = [[0, 0, 0]] * 100001 주의
# => [0] * n은 같은 리스트를 복사하기 때문에
# => 리스트안의 값이 같은 값으로 바뀜
dp=[[0 for _ in range(3)] for i in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 10):
    dp[i][0] = dp[i-1][1]%1000000009 + dp[i-1][2]%1000000009
    dp[i][1] = dp[i-2][0]%1000000009 + dp[i-2][2]%1000000009
    dp[i][2] = dp[i-3][0]%1000000009 + dp[i-3][1]%1000000009
    print(dp[:11])

for i in range(t):
    case = int(input())
    print(sum(dp[case])%1000000009)