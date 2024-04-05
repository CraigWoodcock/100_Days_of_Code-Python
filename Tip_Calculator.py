#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = float(input("what was the total of the bill? "))
tip = int(input("how much would you like to tip (%)? 10, 12 or 15 "))
people = int(input("how many people should the bill be split between? "))
total_inc_tip = round((((tip/100)+1)*total_bill)/people,2)
print(total_inc_tip)
