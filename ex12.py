num1=int(input("enter first number:"))
original=num1
reverse=0
while num1>0:
    digit=num1%10
    print(digit,end=" ")
    reverse=reverse*10+digit
    num1=num1//10



