# 1+11+111+......n-terms
n = int(input("Enter the value of n: "))
sumi = 0
i = 1
num = 1

while i <= n:
    sumi += num
    num = num * 10 + 1
    i += 1

print("The sum of the series is:", sumi)