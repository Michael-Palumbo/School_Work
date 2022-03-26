def merge(numbers, i, j, k):
    merged_size = k - i + 1
    merged_numbers = []
    for l in range(merged_size):
        merged_numbers.append(0)
    merge_pos = 0
    left_pos = i
    right_pos = j + 1
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k):
    j = 0
    if i < k:
        j = (i + k) // 2
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        merge(numbers, i, j, k)


numbers = [420, 69, 123, 456]
print ('UNSORTED:', end=' ')
for num in numbers:
    print (str(num), end=' ')
print()
merge_sort(numbers, 0, len(numbers) - 1)
print ('SORTED:', end=' ')
for num in numbers:
    print (str(num), end=' ')
print()
