# prime or not

n = int(input("Enter a number to check if it's prime or not : "))
i = 2
count = 0
while i <= n:
    if n % i == 0:
        count += 1
    i += 1

if count == 1:
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")