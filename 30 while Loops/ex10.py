i=int(input("Enter the value Till where the loop works : "))
x=int(input("Enter the value of x : "))
j=1
sum=0
while i>0:
    if j==3:
        sum-=x**j
    else:
        sum+=x**j
    i-=1
    j+=2

print(sum)