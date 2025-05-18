amount=int(input("Enter the amount "))
note1=amount//100
note2=(amount%100)//50
note3=(amount%100)%50//10
print("Number of Rs100 notes=",note1)
print("Number of Rs50 notes=",note2)
print("Number of Rs10 notes=",note3)