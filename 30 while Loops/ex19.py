# palindrome : 121, 12321, etc... {symmetric}

n = int(input("Enter a number to check if it's palindrome or not : "))
num = n            # num is taken because n is used in the loop and it's value changes
reverse_num = 0
remainder = 0

while n > 0:
    remainder = n % 10
    reverse_num = reverse_num * 10 + remainder
    n //= 10

if num == reverse_num:
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")

