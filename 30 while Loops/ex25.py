# lcm of two numbers

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
divisor = 1

lcm = max(num1, num2)
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1
    
print(f"LCM of {num1} and {num2} is {lcm}.")







