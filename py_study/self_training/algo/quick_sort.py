def qsort(numbers):
    if len(numbers) == 0:
        return []
    else:
        return qsort([i for i in numbers[1:] if i <= numbers[0]]) + [numbers[0]] + \
               qsort([i for i in numbers[1:] if i > numbers[0]])


seq = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]

print(qsort(seq))
