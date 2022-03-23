def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end= '')

bin = int(input("Enter a number to be converted to binary: "))

convertToBinary(bin)
