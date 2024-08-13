def common_numbers_sorted(listA, listB):
    common_numbers = set(listA) & set(listB)
    sorted_common_numbers = sorted(common_numbers)
    print(" ".join(map(str, sorted_common_numbers)))

listA = [18, 2, 90, 3, 5]
listB = [2, 86, 42, 5, 7]
common_numbers_sorted(listA, listB)