def calculate(x: float, y: float, operation="a") -> float:
    def addition(x, y, operation="a"):
        rez = x + y
        print(f"{x} + {y} = {round((rez), 2)}")

    def subtraction(x, y, operation="s"):
        rez = x - y
        print(f"{x} - {y} = {round((rez), 2)}")

    def division(x, y, operation="d"):
        if y != 0:
            rez = x / y
            print(f"{x} / {y} = {round((rez), 2)}")
        else:
            print("You can't divide by zero!")

    def multiplication(x, y, operation="m"):
        rez = x * y
        print(f"{x} * {y} = {round((rez), 2)}")

    if operation == "a":
        addition(x, y, operation="a")

    if operation == "s":
        subtraction(x, y, operation="s")

    if operation == "d":
        division(x, y, operation="d")

    if operation == "m":
        multiplication(x, y, operation="m")

    if operation not in "asdm":
        print('Error. This operation does not exist')


x = float(input("Enter digit: "))
y = float(input("Enter digit: "))

print(f"\nChoose actions:\n a - addition,\n s - subtraction, \n d - division, \n m - multiplicftion")

operation = str(input("\nEnter operation: "))
calculate(x, y, operation)


