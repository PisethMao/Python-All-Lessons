numbers = [1, 2, 3, 4, 5, 6]

# 1. Access item
print(numbers[0])

# 2. Change item
numbers[1] = 25
print(numbers)

# 3. Add item
numbers.append(50)
print(numbers)

# 4. Insert item
numbers.insert(1, 15)
print(numbers)

# 5. Delete item
numbers.remove(25)
print(numbers)

# 6. Delete by index
numbers.pop(0)
print(numbers)

# 7. Loop through array
for num in numbers:
    print(num)

# 8. Find length
print(len(numbers))

# 9. Sort
numbers.sort()
print(numbers)

# 10. Search
print(30 in numbers)