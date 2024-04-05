
#take an age as an input.
age = input("What is your age? \n")

#subtract the age from 90 and then multiply by weeks per year(52).
remaining = (90 - int(age)) * 52

#print the result in an f-string so we do not have to convert from an int to a str().
print(f"You have {remaining} weeks left")
