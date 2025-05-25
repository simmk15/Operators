a=int(input("Enter the 1st number="))
b=int(input("Enter the 2nd number="))
c=int(input("Enter the 3rd number="))
if a>b or a<c:
    print("i'm using the OR operator")
elif a<b and a>c:
    print("i'm using AND condition")
else:
    print("It's different")