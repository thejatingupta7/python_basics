# find sum of an A.P. series

a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms : "))
d = int(input("Enter the common difference : "))

i = 1
add = 0
while i <= n:
    term = a + (i - 1) * d
    add += term
    i += 1

print(f"Sum of the AP : ", add)
