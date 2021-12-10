#title text
print("Python Calculator")
print("By: Sam Crowder")
print("if answer does not appear try clicking enter again!")
#variables
num1 = float(input("Put your first number in here!| "))
operator = input("Select operator!| ")
num2 = float(input("Put your second number in here!| "))

#if else statements
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid input!")