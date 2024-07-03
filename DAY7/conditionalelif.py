import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will chage you 2 dollar a day")
elif  type == "t2.medium":
    print("it will chage you 4 dollar a day")
elif  type == "t2.xlarge":
    print("it will chage you 8 dollar a day")
else:
    print("please provide a valid instance type")