def check_numbers_seen_before(numbers):
    seen_numbers = set()
    for number in numbers:
        if number in seen_numbers:
            print("YES")
        else:
            print("NO")
            seen_numbers.add(number)

numbers = [1, 3, 8, 35, 4, 2, 3]
check_numbers_seen_before(numbers)