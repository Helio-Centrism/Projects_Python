print("Welcome to the tip calculator!")

# Get the total bill amount
total_bill = float(input("What was the total bill? $"))

# Get the tip percentage and convert it to a decimal
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_value = tip_percentage / 100

# Get the number of people to split the bill
number_of_people = int(input("How many people to split the bill? "))

# Calculate the total amount including tip
total_with_tip = total_bill * (1 + tip_value)

# Calculate each person's share
amount_per_person = total_with_tip / number_of_people

# Round to 2 decimal places
amount_per_person = round(amount_per_person, 2)

# Print the result
print(f"Each person should pay: ${amount_per_person}")
