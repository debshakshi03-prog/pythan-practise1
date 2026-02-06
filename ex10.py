list1=[10,20,30,40,35]
list2=[20,80,70,60,40]
result=[]
for i in list1 :
    if i%2!=0:
        result.append(i)
for i in list2:
    if i%2==0:
        result.append(i)
print (result)
