from functools import reduce

name = "Piseth Mao"
upper = lambda s: s.upper()
print(upper(name))

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))
print(check(-3))
print(check(0))

number = lambda x: "Even" if x % 2 == 0 else "Odd"
print(number(4))
print(number(7))

func = [lambda arg = x: arg * 10 for x in range(1, 5)]
for num in func:
    print(num())

calc = lambda x, y: (x + y, x * y)
result = calc(1, 2)
print(result)

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(list(even))

a = [1, 2, 3, 4, 5, 6]
double = map(lambda x: x * 2, a)
print(list(double))

b = [1, 2, 3, 4, 5, 6]
mul = reduce(lambda x, y: x * y, b)
print(mul)