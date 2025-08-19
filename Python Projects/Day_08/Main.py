def value():
    num1=float(input("What's the first number! : "))
    calculator(num1)


def calculator(num1):
    operand=input("Pick an operation : ( + - * / ) : ")
    num2=float(input("What's the next number : "))
    if operand=="+":
        result=num1+num2
        print(f"{num1} + {num2} = {result}")
    elif operand=="-":
        result=num1-num2
        print(f"{num1} - {num2} = {result}")
    elif operand=="*":
        result=num1*num2
        print(f"{num1} * {num2} = {result}")
    elif operand=="/":
        result=num1/num2
        print(f"{num1} / {num2} = {result}")
    choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if choice=="y":
        calculator(result)
    else:
        value()




print("Welcome to Calculator !!")
value()
