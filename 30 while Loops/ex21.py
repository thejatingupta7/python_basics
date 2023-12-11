# decimal to binary conversion without array

num = int(input("Enter a decimal number: "))
binary = 0
digit = 1

while num > 0:
    binary += (num % 2) * digit
    digit *= 10
    num //= 2

print("Binary number:", binary)

