arr = [1, 1, 0, -1, -1]

positive = 0
negative = 0
zero = 0

for value in arr:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        zero += 1

print(f'{positive/len(arr):5f}')
print(f'{negative / len(arr):5f}')
print(f'{zero / len(arr):5f}')
