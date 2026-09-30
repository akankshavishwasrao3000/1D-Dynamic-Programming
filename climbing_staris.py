'''
DP Problem 2 — Climbing Stairs
Problem

You are climbing a staircase with N steps.

You can climb either:

1 step at a time
2 steps at a time

Find the number of different ways to reach the top.

Example
Input:
5

Output:
8
'''

import sys

def solve():
    data=list(map(int,sys.stdin.read().split()))

    if not data:
        return

    n=data[0]

    dp=[0]*(n+1)

    dp[0]=1

    if n>=1:
        dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        print(i)

    print(dp[n])

if __name__=="__main__":
    solve()            