# Find Payment of employees & if Worked +40 Hours give 1.5 Rate
SHours = input("Enter Hours:")
try:
    FHours = float(SHours)
except:
    print("Hours You Entered Is Invalid -Might be String not number-")
    FHours = -1
SRatePerHours = input("Enter The Rate per Hour: ")
try:
    FRatePerHours = float(SRatePerHours)
except:
    print("Rate Per Hours You Entered Is Invalid -Might be String not number-")
    FRatePerHours = -1
if FHours > 40:
    Pay = (40*FRatePerHours)+((FHours-40)*(FRatePerHours*1.5))
else:
    Pay = FRatePerHours * FHours
if FRatePerHours == -1 or FHours == -1:
    print("Finished with errors")
else:
    print("Pay: ", Pay)
