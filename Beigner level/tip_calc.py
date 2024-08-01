print("Welcome to the tip calculator!")
total_bill = float(input("Enter the total bill? $"))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_value = float(tip) / 100 

spilt_bill = int(input("How many people do you want to spilt the bill?"))

bill_split = (total_bill / spilt_bill) * tip_value

each_split = round(bill_split, 2)
print(f"The total ammount each person has to pay is $ {each_split} including tip")