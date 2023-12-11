# decimal to octal without array

n = int(input("Enter a decimal number : "))

octal_num = 0
i = 1

while n > 0:
    rem = n % 8
    octal_num += rem * i
    n //= 8
    i *= 10

print(f"The octal equivalent is {octal_num}")
