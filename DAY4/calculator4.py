import sys

def add(num1 , num2):
     add = num1 + num2
     return add

def sub(num1 , num2):
    sub = num1 - num2
    return sub

def mul(num1 , num2):
   mul = num1 * num2
   return mul

num1 = int(sys.argv[1])  
operation = sys.argv[2]
num2 = int(sys.argv[3])

if operation == "add":
   output = add(num1 , num2)
   print(output)


if operation == "sub":
   output = sub(num1 , num2)
   print(output)


if operation == "mul":
   output = mul(num1 , num2)
   print(output)


