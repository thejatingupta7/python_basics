# perfect numbers: 6 = 1*2*3 = 1+2+3

n = int(input("Enter a number to check if it's perfect or not : "))
i = 1
sum1 = 0

while i < n:
    if n % i == 0:
        sum1 += i
    i += 1
if sum1 == n:
    print("The number is perfect.")
else:
    print("The number is not perfect")
