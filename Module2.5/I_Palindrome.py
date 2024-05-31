
def is_palindrome(num):
    return num == (num)[::-1]
 
 
value = input()
res=int(value[::-1])
val=is_palindrome(value)
if val:
    print(value)
    print("YES")
else:
    print(res)
    print("NO")




