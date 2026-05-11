def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            if letter.isupper():
                translation = translation + "Piseth"
            else:
                translation = translation + "piseth"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))