# file = open("libs.txt", "r")
# read_file = file.read()
# print(read_file)
#
# print(type(file))

# try:
#     number = str("asdfasdf")
# except ValueError as b:
#     print("Error: Invalid input", b)


number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    print("Addition result:", number1 + number2)
elif operation == "-":
    print("Subtraction result:", number1 - number2)
elif operation == "*":
    print("Multiplication result:", number1 * number2)
else:
    try:
        print("Division result:", number1 / number2)
    except ZeroDivisionError:
        print("Invalid operation")
    else:
        print("Division result:", number1 / number2)