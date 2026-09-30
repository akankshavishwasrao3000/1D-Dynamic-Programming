import sys

def solve():
    data=sys.stdin.read().split()

    n=int(data[0])
    arr=[]

    for i in range(1,n+1):
        arr.append(int(data[i]))

    if n==0:
        print(0)
        return
    if n==1:
        print(arr[0])
        return

    dp=[0]*n
    dp[0]=arr[0] 
    dp[1]=arr[1]

    for i in range(2,n):
        if dp[i-1]< dp[i-2]:
            dp[i]=arr[i]+dp[i-1]
        else:
            dp[i]=arr[i]+[i-2]

    if dp[n-1]<dp[n-2]:
        print(dp[n-1])

    else:
        print(dp[n-2])   

if __name__ =="__main__":
    solve()         
