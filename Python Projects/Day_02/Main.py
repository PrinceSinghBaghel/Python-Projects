print("Welcome to tip Calculator")
bill=0
bill=float(input("What was the total bill ? Rs. "))
tip=float(input("How much tip you want to give : 10, 12, or 15 ? "))
bill=bill+(tip/100)*bill
people=float(input("How many people to split the bill ? "))
bill=bill/people
bill=round(bill,2)
print(f"Each person Should pay : Rs. {bill}")