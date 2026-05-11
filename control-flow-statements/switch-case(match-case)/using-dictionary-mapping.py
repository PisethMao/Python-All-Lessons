def one():
    return "One"
def two():
    return "Two"
def three():
    return "Three"
switcher = {
    1: one,
    2: two,
    3: three
}
value = 2
result = switcher.get(value, lambda: "Unknown")()
print(result)