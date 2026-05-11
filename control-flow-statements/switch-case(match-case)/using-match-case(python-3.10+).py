value = 2
match value:
    case 1:
        result = "One"
    case 2:
        result = "Two"
    case 3:
        result = "Three"
    case _:
        result = "Unknown"
print(result)