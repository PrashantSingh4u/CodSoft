num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))

operator = input("Enter Any Arithmetic Operator : ")

match operator:
    case "+":
        print("Sum Of Both Number is :  ",num1+num2)
    case "-":
        print("Subtraction Of Both Number is :  ",num1-num2)
    case "/":
        print("Divison Of Both Number is :  ",num1/num2)
    case "*":
        print("Multiplication Of Both Number is :  ",num1*num2)
    case _:
        print("Entered Operator Is Not Valid For Arithmetic Operations")
