n=int(input("ENTER A NUMBER: "))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum+=i  
    i+=1        
print(sum)