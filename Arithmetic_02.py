#  Program Arithmetic_02.py
#  Written by: Joe Dorward
#  Date: 07/12/2023

#  This program:
#  * asks the user to enter two integers
#  * adds them together
#  * prints the answer to the screen

# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
def main():
  print("\n----------------------------------------")

  FirstNumber = input("Enter first integer: ") # prompt for first number
  SecondNumber = input("Enter second integer: ") # prompt for second number

  print("\nAdding " + str(FirstNumber) + " and: " + str(SecondNumber) + " results in: " + str(int(FirstNumber) + int(SecondNumber)))

  print("----------------------------------------\n")
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------
main()