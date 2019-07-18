sh1 = float(input("Enter first number:"))
sh2 = float(input("Enter second number:"))
sh3 = float(input("Enter third number:"))
 
if (sh1 > sh2) and (sh1 > sh3):
   largest = sh1
elif (sh2 > sh1) and (sh2 > sh3):
   largest = sh2
else:
   largest = sh3
 
print("The largest number is",largest)
