def wordCount(word):
    return len(word)
print(wordCount("Kabayo"))

def cellphoneNumberchecker(number):
    if len(number) == 11 and number.isdigit():
     return True

print(cellphoneNumberchecker(99055414862))

def numberCount(number):
    return len(str(number))


print(numberCount(9313131))