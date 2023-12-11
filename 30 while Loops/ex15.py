# armstrong number : [1634] = { (1**3) + (6**3) + (3**3) + (4**3) }

rang = int(input("Enter a range value to check which numbers till that value are armstrong : "))
for n in range(1, rang+1):
    str1 = str(n)
    exp = len(str1)
    add, i = 0, 0
    while i < exp:
        add += int(str1[i]) ** 3
        i += 1
    if add == n:
        print(f"{n} is an armstrong number.")


