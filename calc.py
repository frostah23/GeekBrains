print("Welcome to calc v0.1")
print("Please, enter two int numbers in correct order")
a = int(input())
b = int(input())
print("Please, choose the operation: enter the correct number of operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input())
if operation == 1:
    print(a, " + ", b, " = ", a+b)
elif operation == 2:
    print(a, " - ", b, " = ", a-b)
    