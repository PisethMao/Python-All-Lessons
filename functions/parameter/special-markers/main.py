def divide(num1, num2, /):
    return num1 / num2
print(divide(1, 2, ))

def student(name, *, age):
    print(name, age)
student("Piseth", age=23)

def example(a, b, /, c, *, d):
    print(a, b, c, d)
example(1, 2, 3, d=4)