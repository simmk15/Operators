smoke=input("Do you see smoke? [YES/NO]=")
fire=input("Do you see fire? [YES/NO]=")
if smoke.lower()=="yes" or fire.lower()=="yes":
    print("Call the firebrigade!")
else:
    print("No need to call the firebrigade")