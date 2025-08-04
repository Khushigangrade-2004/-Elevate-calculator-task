print("------BASIC CALCULATER------")
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))

while True:
    operation=input("enter operation between '+','-'.'*','/','Exit' ")
    if operation == '+':
        print(num1+num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
    elif operation =='/':
        print(num1/num2)
    elif operation =='Exit':
        print("THANKS FOR USING CALCULATER....")
        break
    else:
        print("invalid operation!")