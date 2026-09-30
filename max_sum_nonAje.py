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

    if arr[0]>arr[1]:
        dp[1]=arr[0]
    else:
        dp[1]=arr[1]    

    for i in range(2,n):
        take=arr[i]+dp[i-2]  
        skip=dp[i-1]  

        if take > skip:
            dp[i]=take
        else:
            dp[i]=skip
    print(dp[n-1])

if __name__=="__main__":
    solve()                

    

    

















