c = str(input("Enter an alphabet: "))

isLowercaseVowel = (c == "a" or c == "e" or c == "i" or c == "o" or c == "u")
isUppercaseVowel = (c == "A" or c == "E" or c == "I" or c == "O" or c == "U")

if isLowercaseVowel or isUppercaseVowel:
    print(c + " is a vowel")
else:
    print(c + " is a consonant")
