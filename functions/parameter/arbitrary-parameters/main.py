def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(add_numbers(2, 3, 4, 5))
print(add_numbers(1, 2, 3))