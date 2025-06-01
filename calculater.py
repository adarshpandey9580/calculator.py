a=int(input ("enter first number:"))
b=int(input ("enter second number:"))
print("choice: 1:addition,2: subtraction,3: multiplication,4: division,5: modulus")
choice=int(input("please enter your choice:"))
if choice==1:
    print(a+b)
if choice ==2:
    print(a-b)
if choice ==3:
    print(a*b)    
if choice ==4:
    print(a/b)    
if choice == 5:
    print(a%b)