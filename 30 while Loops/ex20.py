# display all integers & their sum from 100-200 which are divisible by 9

i = 100
add = 0
while i < 201:
    if i % 9 == 0:
        add += i
        print(i, end=", ")
    i += 1
print("\nThe sum of above numbers is : ", add)
