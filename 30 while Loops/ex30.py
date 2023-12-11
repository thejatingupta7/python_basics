# Binary to Octal

num = int(input("Enter a binary number : "))

# binary to decimal
decimal = 0
exp = 0
while num > 0:
    decimal += (num % 10) * (2 ** exp)
    exp += 1
    num //= 10

# decimal to octal
octal_num = 0
i = 1
while decimal > 0:
    rem = decimal % 8
    octal_num += rem * i
    decimal //= 8
    i *= 10

print(f"The octal equivalent is {octal_num}")

