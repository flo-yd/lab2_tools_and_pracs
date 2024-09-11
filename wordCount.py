def wordCount(word):
    return len(word)
print(wordCount("Kabayo"))

def cellphoneNumberchecker(number):
    if len(number) == 11 and number.isdigit():
     return True

print(cellphoneNumberchecker(99055414862))