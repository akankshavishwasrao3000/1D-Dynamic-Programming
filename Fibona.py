'''
Find the Nth Fibonacci number.

Input:
6

Output:
8
'''

import sys

def solve():
    data= sys.stdin.read().split()

    if not data:
        return

    n=int(data[0])
    if n == 0:
        print(0)
        return

    dp = [0]*(n+1) #if n=6 so 6+1=7 zeros will add .it will our positions num will add one by one

    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    print(dp[n])

if __name__=="__main__":
    solve()        





