


a = "apple"
b = "ball"
z = "zebra"

def addNumber (a,b):
   a=int(input("Enter the first number: "))
   b=int(input("Enter the second number: "))
   add = a + b
   return(add)

def subtractNumber (a,b):
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    minus = a - b
    return (minus)

def multiplyNumber (a,b):
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    times = a * b
    return (times)


def divideNumber (a,b):
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    divide = a / b
    return (divide)

def modularNumber (a,b):
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    modular = a % b
    return (modular)

def operation (ch):
    ch=input("Enter any of these operator for operation +, -, *, /, % ")
    if ch=='+':
     print(addNumber(0,0))
    elif ch=='-':
        print(subtractNumber(0,0))
    elif ch=='*':
        print(multiplyNumber(0,0))
    elif ch=='/':
        print(divideNumber(0,0))
    elif ch=='%':
        print(modularNumber(0,0)) 
    else:
       print("char is not supported");


operation(0)




