
i=0
sum=0
while i<10:
    n=int(input("ENTER A NUMBER: "))
    sum+=n
    i+=1
    if n==0:
        break
print("the sum is: ")
print(sum)
print("THE AVERAGE IS: ")
avg=sum/(i-1)
print(avg)