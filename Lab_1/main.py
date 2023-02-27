import say_hello
import calculator

say_hello.print_hello()

num1 = None
num2 = None

while True:
    a = input("enter the first number: ")

    if a.isdigit():
        num1 = int(a)
        break

while True:
    b = input("enter the second number: ")

    if b.isdigit():
        num2 = int(b)
        break

operation = input("choose an operation (add, sub, mult or div): ")
result = calculator.calculate(num1, num2, operation)
print("result:", result)
