# Octal to decimal without array
n = int(input("Enter an octal number : "))

decimal = 0
i = 1
exp = 0

while n > 0:
    digit = n % 10
    rem = (8**exp) * digit
    decimal += rem
    n //= 10
    exp += 1

print(f"The decimal equivalent is {decimal}")
