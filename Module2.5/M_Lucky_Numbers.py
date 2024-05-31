
A,B = map(int ,input().split())

list = []

for i in range(A,B+1):
    flag=True
    for j in str(i):
        if not (j== '4' or j=='7'):
            flag=False
            break
    if flag==True:
        list.append(i)
if len(list):
    for i in list:
        print(i,end=" ")
else:
    print(-1) 
