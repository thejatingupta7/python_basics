# first n terms of the fibonacci series  : 0,1,1,2,3,5,......

n = int(input("Enter the number of terms : "))

previous = 0
current = 1

print(previous, end=", ")
print(current, end=", ")

i = 2
while i < n:
    next_num = previous + current
    print(next_num, end=", ")
    previous = current
    current = next_num
    i += 1
