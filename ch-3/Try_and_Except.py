StrAge = input("Input Your Age As An Integer: ")
try:
    IntAge = int(StrAge)
except:
    IntAge = -1
if IntAge == -1:
    print("Invalid Input - Your Input is not Integer - ")
else:
    print("Your Age Is", IntAge)
