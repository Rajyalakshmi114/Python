import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create the instance for you")
else:
    print("your is not t2.micro, so we cannot create")

