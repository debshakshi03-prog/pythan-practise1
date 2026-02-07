p=int(input("enter the number:"))
i=2
while p>1:
    if p%i==0:
        print(i,end="  ")
        p=p//i
    else:
        i=i+1 
