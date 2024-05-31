N=int(input())
Array =list(map(int,input().strip().split()))[:N]

reversed = Array[::-1]

if Array==reversed:
    print("YES")
else:
    print("NO")


