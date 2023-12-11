# armstrong number : [1634] = { (1**4) + (6**4) + (3**4) + (4**4) }

n = int(input("Enter a value to check if it's armstrong or not : "))
str1 = str(n)
exp = len(str1)
add, i = 0, 0
while i < exp:
    add += int(str1[i])**exp
    i += 1
    
if add == n:
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")