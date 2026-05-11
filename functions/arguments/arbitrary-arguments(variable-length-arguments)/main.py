def show_numbers(*args):
    print(args)
show_numbers(1, 2, 3, 4, 5, 6, 7)
show_numbers(1, 2, 3, 4, 5)

def total(*numbers):
    sum_value = 0
    for n in numbers:
        sum_value += n
    print(sum_value)
total(1, 2, 3, 4)
total(1, 2, 3, 4, 5)

def student(**kwargs):
    print(kwargs)
student(name="Michael", age=21)

def info(**data):
    for key, value in data.items():
        print(key, " = ", value)
info(name="Michael", age=21)

def demo(*args, **kwargs):
    print(args)
    print(kwargs)
demo(1, 2, 3, name="Michael", age=21)