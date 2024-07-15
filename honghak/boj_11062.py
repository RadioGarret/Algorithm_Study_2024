import sys
sys.stdin = open("honghak/boj_11062_input.txt", "r")


T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    
    dp = [[[-1 for _ in range(2)] for _ in range(N)] for _ in range(N)] # N -> N -> turn
    
    def dfs(start, end, is_k):
        if start > end:
            return 0
        
        if dp[start][end][is_k] != -1:
            return dp[start][end][is_k]
        
        if is_k:
            dp[start][end][is_k] = max(dfs(start+1, end, 0) + arr[start], dfs(start, end-1, 0) + arr[end])
        else:
            dp[start][end][is_k] = min(dfs(start+1, end, 1), dfs(start, end-1, 1))
        
        return dp[start][end][is_k]
    
    print(dfs(0, N-1, 1))