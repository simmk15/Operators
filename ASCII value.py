char=(input("Enter an alphabet-"))
if len(char) !=1:
    print("ERROR! Only 1 alphabet can be entered.")
else:
    ans=ord(char)
    print("The ASCII value for "+char , "is",ans)