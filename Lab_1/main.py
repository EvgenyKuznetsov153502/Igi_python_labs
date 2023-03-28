import say_hello
import calculator
import even_list
from random import randint

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

lst = [randint(1, 20) for i in range(20)]
print("initial list: ", lst)
print("sorted list: ", even_list.even_list(lst))
