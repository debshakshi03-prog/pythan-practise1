p=int(input("enter the prime  number"))
count=0
for i in range(p+1,p+10):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=1
        if count==1:
           q=i
           print(q,end="  ")
if q-p==2:
    print("it is twin:",end="  ")
else:
    print("it is not twin:",end="  ")
