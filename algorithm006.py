arr = [1, 2, 3, 4, 5]

no_minimum_sum = 0
no_maximum_sum = 0


arr_no_max = arr.copy()
arr_no_max.remove(max(arr))

arr_no_min = arr.copy()
arr_no_min.remove(min(arr))


for i in arr_no_max:
     no_maximum_sum += i

for i in arr_no_min:
     no_minimum_sum += i

print(f'{no_maximum_sum} {no_minimum_sum}')
print(arr)




