
n = int(input("Enter a number till you want squares and their sum : "))
i = 1
add = 0
while i <= n:
    print(f"The square of {i} is ", i**2)
    add += i**2
    i += 1
print(f"The sum of squares of numbers is {add}")
