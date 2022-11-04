# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class Solution:
    def climbStairs(self, n: int) -> int:
        max_twos = n // 2
        result   = 0
        for twos in range(max_twos+1):
            ones  = n - twos * 2
            tot   = ones + twos

            result += factorial(tot)/(factorial(ones) * factorial(twos))

        return int(result)
