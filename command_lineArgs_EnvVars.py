import sys
import os

print(os.getenv("password"))

def addition(num1, num2):
    add= num1 + num2
    return add
def substraction(num1, num2):
    sub= num1 - num2
    return sub
def multiple(num1, num2):
    mul= num1 * num2
    return mul
def division(num1, num2):
    div= num1 / num2
    return div
def modulus(num1, num2):
    mod= num1 % num2
    return mod

anynum1 = int(sys.argv[1])
operator = sys.argv[2]
anynum2 = int(sys.argv[3])

if operator == "addition":
    print(addition(anynum1, anynum2))
elif operator == "substraction":
    print(substraction(anynum1, anynum2))
elif operator == "multiple":
    print(multiple(anynum1, anynum2))
elif operator == "division":
    print(division(anynum1, anynum2))
elif operator == "modulus":
    print(modulus(anynum1, anynum2))
else:
    print("please enter valid number")