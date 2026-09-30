import sys

def solve():
    data=sys.stdin.read().split()

    n=int(data[0])

    hights=[]
    for i in range(1,n+1):
        hights.append(int(data[i]))

    if n <=1:
        print(0)
        return    

    dp=[0]*n
    dp[0]=0

    for i in range(1,n):
        one_jump=dp[i-1]+abs(hights[i]-hights[i-1])

        two_jump=float('inf')

        if i>=2:
            two_jump=dp[i-2]+abs(hights[i]-hights[i-2])

        if one_jump <two_jump:
            dp[i]=one_jump
        else:
            dp[i]=two_jump

    print(dp[n-1])

if __name__=="__main__":
    solve()






