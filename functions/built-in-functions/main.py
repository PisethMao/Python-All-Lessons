# As of recent Python versions, there are approximately 71 built-in functions.
# 49 is useful.

# 1
print("Learning Python!!!")
# 2
name = "Python"
print(len(name))
# 3
print(type(5))
print(type("Hello"))
# 4
age = "25"
print(int(age))
# 5
name = input("Enter your name: ")
print("Hello, " + name + "!!!")
# 6
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))
# 7
print(max([3, 6, 2]))
print(min([3, 6, 2]))
# 8
print(sorted([5, 2, 9]))
# 9
for i in range(3):
    print(i)
# 10
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(index, color)
# 11
names = ["Piseth Mao", "Sophaneth Mao"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}.")
# 12
print(abs(-10))
# 13
print(round(3.14159, 2))
# 14
print(all([True, False, True]))
print(any([True, False, True]))
# 15
print(dir(str))
# 16
help(len)
# 17
expression = "3 + 5"
print(eval(expression))
# 18
for char in reversed("Python"):
    print(char, end="")
# 19
x = 10
print(isinstance(x, int))
# 20
# nums = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, nums))
# print(squared)
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)
#21
print(dir(__builtins__))