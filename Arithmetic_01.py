#  Program Arithmetic_01.py
#  Written by: Joe Dorward
#  Date: 07/12/2023

#  This program:
#  * asks the user to enter two integers
#  * adds them together
#  * prints the answer to the screen

# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
print("\n----------------------------------------")

FirstNumber = input("Enter first integer: ") # prompt for first number
SecondNumber = input("Enter second integer: ") # prompt for second number

TheAnswer = int(FirstNumber) + int(SecondNumber) # do the addition

print(str(FirstNumber) + " + " + str(SecondNumber) + " = " + str(TheAnswer))

print("----------------------------------------\n")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
