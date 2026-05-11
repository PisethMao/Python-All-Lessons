# one argument
square = lambda x: x * x
print(square(4))

# multiple arguments
multiply = lambda a, b: a * b
print(multiply(3, 5))

# default argument
greet = lambda name="Guest": "Hello " + name
print(greet())

# variable-length positional arguments
total = lambda *nums: sum(nums)
print(total(1, 2, 3))

# keyword arguments
student = lambda **data: data
print(student(name="Piseth", age=20))