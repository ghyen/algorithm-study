import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    lst.append(list(map(int, input().split())))
    lst.append(list(map(int, input().split())))
    
    dp = [[0] * N for i in range(2)]
    dp[0][0] = lst[0][0]
    dp[1][0] = lst[1][0]
    
    for i in range(1, N):
        
        if i > 1:
            dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + lst[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + lst[1][i]
        else:
            dp[0][i] = dp[1][i-1] + lst[0][i]
            dp[1][i] = dp[0][i-1] + lst[1][i]
        
    print(max(dp[1][N-1], dp[0][N-1]))