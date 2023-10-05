"""leetcode 322. 零钱兑换 | medium | dp
给定数组coins（元素代表面额，可认为每种面额的硬币的数量无限）和数值amount（总金额），请找出凑出amount所需最小的硬币数量n，如果凑不出amount则返回-1。    

"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      # 1.定义状态: dp[i], i为金额，取值0～amount
      # 2.初始状态: dp[0] = 0
      # 3.转移方程: dp[i] = min( dp[i-1],dp[i-2]...dp[i-i] )+1
      dp = [float('inf')]*(amount+1)
      dp[0] = 0

      # 4.自底向上计算
      for x in range(min(coins),amount+1):
        for coin in coins:
          dp[x] = min(dp[x], dp[x-coin]+1) if coin <= x else dp[x]
        
      return -1 if dp[amount] == float('inf') else dp[amount]

coins = [1, 2, 5, 10]
amount = 11
sol = Solution()
print(sol.coinChange(coins=coins, amount=amount))

class Sol_fibonacci():
   """
   0,1,1,2,3,5...
   """
   def fibonacci(self, N:int) -> int:
    dp = [float('inf')]*(N+1)
    dp[0], dp[1] = 0, 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]
   
sol_fib = Sol_fibonacci()
print(sol_fib.fibonacci(5))

"""
118. 杨辉三角 | easy | dp
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[-1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            dp[i][0] = 1 
            dp[i][-1] = 1

        for i in range(numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

        return dp
    

"""
5. 最长回文子串 | median | dp
"""
class Sol_Palindrome():
   def longestPalindrome(self, s: str) -> str:
        # 1.定义状态
        max_len = 1
        start, end = 0, 1
        n = len(s)
        dp = [[False]*n for i in range(n)]
        # 对角线上全为True
        for i in range(n):
            dp[i][i] = True
        
        # 2.状态转移方程
        # dp[i][j] = dp[i+1][j-1] if s[i]==s[j] else False

        # 3.自底向上计算
        for L in range(2,n+1):
           # i: 左边界
           for i in range(n):
              # j: 右边界。推导: L = j-i+1 -> j = L+i-1
              j = L+i-1
              if j>=n:
                 break

              if s[i] == s[j]:
                 # 转移方程要求长度至少为4
                 if L >= 4:
                    dp[i][j] = dp[i+1][j-1]
                 else:
                    dp[i][j] = True
              else:
                 dp[i][j] = False
              if dp[i][j] and L > max_len:
                max_len = L
                start = i
                end = i+L
        return s[start:end]

sol_Palindrome = Sol_Palindrome()
s = 'sjsbdbsd'
print(sol_Palindrome.longestPalindrome(s))