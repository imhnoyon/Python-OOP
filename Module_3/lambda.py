# lambda operation
# def doubled(x):
#     return x**2
# print(doubled(10))


doubled = lambda x: x**2
print(doubled(10))

numbers=[10,20,30,40,50]

print(numbers)
# doubled_nums = map(doubled,numbers)
doubled_nums = map(lambda x:x**2, numbers)
print(list(doubled_nums))
