SScore = input("Enter Score: ")
try:
    FScore = float(SScore)
except:
    print("Invalid Input -maybe Value You entered Is Not Number-")
    FScore = -1
if (FScore >= 0.0) and (FScore < 0.6):
    print("F")
elif (FScore >= 0.6) and (FScore < 0.7):
    print("D")
elif (FScore >= 0.7) and (FScore < 0.8):
    print("C")
elif (FScore >= 0.8) and (FScore < 0.9):
    print("B")
elif (FScore >= 0.9) and (FScore <= 1.0):
    print("A")
elif FScore != -1:
    print("Score is Out Of Allowed Range")



