p=int(input("enter the number"))
count=0
for i in range(p+1,p+10):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count=count+1
        if count==1:
            q=i
            print( "next prime number is:",q,end="  ")
        elif count==2:
            r=i
            print( "next prime number is:",r,end="  ")



