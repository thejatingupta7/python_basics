# display number in reverse order

n = int(input("Enter a number: "))

reverse_num = 0
remainder = 0

while n > 0:
    remainder = n % 10
    reverse_num = reverse_num * 10 + remainder
    n //= 10

print("Reversed number:", reverse_num)
