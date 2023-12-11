# Prime number
'''
num = int(input("Enter a number : "))
count = 0
for i in range(2, num):
    if num % i == 0:
        count += 1
if count == 0:
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")



num = int(input("Enter a number : "))
count = 0
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime.")
        break
else:
    print(f"{num} is prime.")



num = int(input("Enter a number : "))
def prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime.")
            break
    else:
        print(f"{num} is prime.")
prime(num)
'''

# Fibonacci [0,1,1,2,3,5,8]
'''
num = int(input("enter terms :"))

prev_num, current_num = 0, 1
print(prev_num, end=", ")
print(current_num, end=", ")
for i in range(num-2):
    next_num = prev_num + current_num
    print(next_num, end=", ")
    prev_num = current_num
    current_num = next_num

# by recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter terms : "))
fibonacci_sequence = fibonacci(n)
print("Fibonacci sequence:", fibonacci_sequence)
'''


# Factorial
'''
num = int(input("Enter a number : "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)


num = int(input("Enter a number : "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(num))
'''

# reverse a string
'''
a = "helloooo"
print(a[::-1])
'''

# Palindrome
'''
n = input("Enter a number : ")
num_reversed = n[::-1]
if n == num_reversed:
    print(f"{n} is palindrome.")
else:
    print(f"{n} is not palindrome.")




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
'''

# Functions
'''
make calculator (+,_,*,/)
'''

# Linear Search
'''
n = int(input("Search Number : "))
a = [1,5,4,77,6]
for i in range(len(a)):
    if n == a[i]:
        print(f"{n} is found at index {i}")
        break
else:
    print(f"{n} is not found")
'''

# Binary Search  {search time = log.base2(n)}
'''
target = int(input("Search Number : "))
arr = [2, 4, 7, 10, 15, 20, 24, 30]
left = 0
right = len(arr) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        found = True
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print(f"Element found at index {mid}.")
else:
    print("Element not found.")
'''

# Bubble sorting
'''
a = input("Enter numbers separated by a space : ").split()
for _ in range(len(a)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            t = a[i]
            a[i] = a[i+1]
            a[i+1] = t
print(a)
'''

# file handling
'''
# Writing to a file
file_path = "example.txt"

# Open the file in write mode
with open(file_path, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is an example file.\n")

# Reading from a file
# Open the file in read mode
with open(file_path, 'r') as file:
    # Read and print the contents of the file
    for line in file:
        print(line, end='')

# Appending to a file
# Open the file in append mode
with open(file_path, 'a') as file:
    file.write("Appending new content.\n")

# Reading from the file again to see the changes
with open(file_path, 'r') as file:
    # Read and print the contents of the file
    for line in file:
        print(line, end='')
'''

# Exception Handling
'''
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2
    print(result)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    print("Program End!")
'''

# OOPs
'''
class calculate:
    def avg(self, x, y):
        return (x+y)/2

object = calculate()

print(object.avg(10, 20))
'''
'''
class Math:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def average(self, x, y):
        return (x + y) / 2

math = Math()
print(math.add(10, 20))
print(math.subtract(10, 20))
print(math.multiply(10, 20))
print(math.divide(10, 20))
print(math.average(10, 20))
'''



