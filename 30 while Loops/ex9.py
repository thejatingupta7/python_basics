n=int(input("ENTER THE RANGE OF NUMBER OF TERMS: "))
sum=0
p=9
i=0
while i<n:
    sum+=p
    p=(p*10)+9
    i+=1
print("sum of series is: ",sum)  