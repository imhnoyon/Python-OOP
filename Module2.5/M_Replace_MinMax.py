value = int(input())
nums = list(map(int,input().strip().split()))[:value]
mn=min(nums)
mx=max(nums)
arr=[]
for i in nums:
    if i==mn:
        arr.append(mx)
    elif i==mx:
        arr.append(mn)
    else:
        arr.append(i)
    
    

print(*arr)



