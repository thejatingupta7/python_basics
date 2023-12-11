# Strong number : {145} = (1! + 4! + 5!) = (1+24+120)

n = int(input("Enter a number : "))
temp = n
fact_sum = 0
while temp > 0:
    digit = temp % 10
    fact, i = 1, 1
    while i <= digit:
        fact *= i
        i += 1
    fact_sum += fact
    temp //= 10

if fact_sum == n:
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")
