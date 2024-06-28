weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "L":
    print("Weight in Kg: " + str(weight / 2.2046))   
elif unit.upper() == "K":
    print("Weight in Lbs: " + str(weight * 2.2046))
else:
    print("Please restart the program and enter a valid unit (K or L)")