#ord
maths=float(input("ENTER MARKS FOR MATHS="))
history=float(input("ENTER MARKS FOR HISTORY="))
physics=float(input("ENTER MARKS FOR PHYSICS="))
geography=float(input("ENTER MARKS FOR GEOGRAPHY="))
chemistry=float(input("ENTER MARKS FOR CHEMISTRY="))
avg=(maths+history+physics+geography+chemistry)/5
print("Your average is=",avg)
if avg<10:
    print("Your grade is F")
elif avg>=10 and avg<30:
    print("Your grade is D")
elif avg>=30 and avg<50:
    print("Your grade is C")
elif avg>=50 and avg<65:
    print("Your grade is B")
elif avg>=65 and avg<80:
    print("Your grade is A")
else:
    print("Your grade is A+")
