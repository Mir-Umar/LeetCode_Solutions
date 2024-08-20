"""
1140. Stone Game II
Solved
Medium
Topics
Companies
Hint
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
    
        # Suffix sums to calculate sum of stones from pile i to the end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # DP table
        dp = [[0] * (n + 1) for _ in range(n)]
        
        # Bottom-up calculation of dp table
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                max_stones = 0
                for x in range(1, min(2 * m, n - i) + 1):
                    if i + x >= n:
                        max_stones = suffix_sum[i]
                    else:
                        max_stones = max(max_stones, suffix_sum[i] - dp[i + x][max(m, x)])
                dp[i][m] = max_stones
        
        # The result is the maximum stones Alice can get starting from the first pile with M = 1
        return dp[0][1]
