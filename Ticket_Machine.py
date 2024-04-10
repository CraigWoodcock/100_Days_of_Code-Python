#If Statements
# check that someones height is over 120cm.


# print("Welcome to the Rollercoaster!!")
# height = int(input("What is your height in cm?: \n"))
# if height <= 119:
#     print("You aren't tall enough to ride this RollerCoaster.")
# else:
#     print("You are tall enough to ride the RollerCoaster.")

#Nested If Statements
#check to see if someone is over 120cm, assign different prices for adult/child tickets

print("Welcome to the Rollercoaster!! \n")
print("You Must Be 120cm or Taller to Ride!! \n")
height = int(input("What is your height in cm?: \n"))

ticket_price = 0
ticket_type = ""
photo_price = 3

if height >= 120:
    print("You can ride this RollerCoaster.")
    age = int(input("What is your age?: \n"))
    if age < 12:
        ticket_type = "CHILD"
        ticket_price = 5
        print(f"the cost of your {ticket_type} ticket is ${ticket_price} \n")
    elif age <=18:
        ticket_type = "JUNIOR"
        ticket_price = 7    
        print(f"the cost of your {ticket_type} ticket is ${ticket_price} \n")
    elif age >= 45 and age <= 55:
        ticket_type = "FREE"
        print(f"The cost of your {ticket_type} ticket is ${ticket_price} \n")
    else:
        ticket_type = "ADULT"
        ticket_price = 12
        print(f"The cost of your {ticket_type} ticket is ${ticket_price} \n")
    
    print("Photos cost $3. ")
    photo_required = input("Would you like a photo with you ticket? Y or N. \n").lower()
    total_price = ticket_price
   
    if photo_required == "Y".lower():
        total_price = ticket_price+photo_price
    #     print(f"The total cost of your photo plus your {ticket_type} ticket is ${total_price}")
    # else:
    print(f"The total price to pay is ${total_price}")

else:
    print("Sorry, You aren't tall enough to ride the RollerCoaster.")
