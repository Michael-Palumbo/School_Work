def partition(numbers, i, k):
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    done = False
    l = i
    h = k
    while not done:
        while numbers[l] < pivot:
            l = l + 1
        while pivot < numbers[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
    return h


def quicksort(numbers, i, k):
    j = 0
    if i >= k:
        return
    j = partition(numbers, i, k)
    quicksort(numbers, i, j)
    quicksort(numbers, j + 1, k)
    return


numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print ('UNSORTED:', end=' ')
for num in numbers:
    print (str(num), end=' ')
print()
quicksort(numbers, 0, len(numbers) - 1)
print ('SORTED:', end=' ')
for num in numbers:
    print (str(num), end=' ')
print()
