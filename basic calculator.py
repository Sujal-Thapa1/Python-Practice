
def calculator():
    """
    The function `calculator` takes two user input numbers and performs addition, subtraction,
    multiplication, or division based on the user's choice.
    """
    a=int(input("Enter the 1st number"))
    b=int(input("Enter the 2nd number"))
    print("Choose an Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operator=input("What operation you would like to do?")
    if operator== "1":
        sum=a + b
        print(f"The addition of {a} and {b} is {sum}")

    elif operator== "2":
        sub=a-b
        print(f"The subtraction of {a} and {b} is {sub}")
    elif operator== "3":
        multiply=a*b
        print(f"The multiplication of {a} and {b} is {multiply}")
    elif operator== "4":
        div=a/b
        print(f"The division of {a} and {b} is {div}")
    else:
        print("Enter a valid operation")

calculator()