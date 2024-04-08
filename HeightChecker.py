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

print("Welcome to the Rollercoaster!!")
height = int(input("What is your height in cm?: \n"))

ticket_price = 0
ticket_type = ""

if height >= 120:
    print("You can ride this RollerCoaster.")
    age = int(input("What is your age?: \n"))
    if age <=18:
        ticket_type = "CHILD"
        ticket_price = 7
        print(f"the cost of your {ticket_type} ticket is ${ticket_price}")
    else:
        ticket_type = "ADULT"
        ticket_price = 12
        print(f"The cost of your {ticket_type} ticket is ${ticket_price}")
else:
    print("You aren't tall enough to ride the RollerCoaster.")
