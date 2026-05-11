list1 = ["C", "C++", "Python", "C#", "Java", "Javascript"]
i = 0
print("Printing list items using while loop")
size = len(list1)
while i < size:
    print(list1[i])
    i += 1
i = 0
print("Printing list items using do while loop")
while True:
    print(list1[i])
    i += 1
    if i < size and len(list1[i]) < 10:
        continue
    else:
        break