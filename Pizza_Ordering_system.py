print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: \n").lower()  
add_pepperoni = input("Do you want pepperoni? Y or N \n") .lower() 
extra_cheese = input("Do you want extra cheese? Y or N \n").lower() 

price = 0

if size == "L".lower():
  price = 25
elif size == "M".lower():
  price = 20
else:
  price = 15

if add_pepperoni == "Y".lower():
    if size == "L".lower():
      price += 3
    elif size == "M".lower():
      price += 3
    else:
      price += 2

if extra_cheese == "Y".lower():
  price +=1
  
print(f"Your final bill is: ${price}.")