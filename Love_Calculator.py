print("The Love Calculator is calculating your score...")

#take in first name
name1 = input("What is your name?")

#take in second name
name2 = input("What is their name?")

# concatenate the two names and store as a variable
name_lower = name1.lower()+name2.lower() 

# count instances of each letter in the word true
t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")

#add them up and multiply by 10
true_total = (t+r+u+e)*10

#count instances of each letter in the word love
l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")

# add them together
love_total = l+o+v+e
#now add true_total and love_total to give the love score
total = true_total+love_total

#print different message depending on score.

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <=50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
