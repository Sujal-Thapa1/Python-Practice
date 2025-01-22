#Function to check if the given number is even or odd
def even_odd_check():
    num=int(input("Enter a number"))
    if num%2==0:
        print(f"Yes {num} is a even number")
    else:
        print(f"No {num} is  a odd number")

even_odd_check()