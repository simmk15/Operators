char=input("Enter your Character=")
if char>='a' and char<='z':
    print(char+" is an ALPHABET.")
elif char>='A' and char<='Z':
    print(char+" is an ALPHABET.")
elif char>='0' and char<='9': 
    print("NOT AN ALPHABET!")
    print(char, "is a DIGIT.")
else:
    print("NOT AN ALPHABET!")
    print(char,"is a SPECIAL CHARACTER.")