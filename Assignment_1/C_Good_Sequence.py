N = int(input())
numbers = list(map(int, input().split()))

freq_count = {}
remove = 0

for num in numbers:
    if num in freq_count:
        freq_count[num] += 1
    else:
        freq_count[num] = 1

for key, value in freq_count.items():
    if value > key:
        remove += value - key
    elif value < key:
        remove += value

print(remove)
