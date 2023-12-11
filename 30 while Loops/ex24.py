# lcm of two numbers using hcf

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
hcf = 0
divisor = 1

while divisor <= num1 and divisor <= num2:
    if num1 % divisor == 0 and num2 % divisor == 0:
        hcf = divisor
    divisor += 1

lcm = int((num1 * num2)/hcf)                     # formula
print(f"LCM of {num1} and {num2} is {lcm}.")