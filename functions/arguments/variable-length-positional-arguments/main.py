def numbers(*args):
    print(args)
numbers(1, 2, 3)

def total(*nums):
    result = 0
    for num in nums:
        result += num
    print(result)
total(10, 20)
total(1, 2, 3, 4, 5)