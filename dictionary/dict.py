user = {
    "name": "Piseth Mao",
    "age": 20,
    "city": "Phnom Penh",
    "color": ["blue", "green", "red"]
}
thisdict = dict(name="Piseth Mao", age=20, city="Phnom Penh")
user["color"] = ["black"]
del user["color"]
print(user)
print(user["name"])
print(len(user))
print(type(user))
print(thisdict)