# binary to decimal 1010 = 10

num = int(input("Enter a binary number : "))
decimal = 0
exp = 0

while num > 0:
    decimal += (num % 10) * (2 ** exp)
    exp += 1
    num //= 10

print("Decimal number:", decimal)

