# Take in height and wight as inputs

height = input("enter height in meters: \n")
weight = input("enter weight: \n")

#convert height to a float and use exponent operator to square the height.
#convert the weight to an int and divide by the height squared.
#store this value as a variable called result

result = int(weight)/(float(height)**2)


#convert the result into an int so it is returned as a whole number.
#store the value as a variable called bmi.
#print the bmi.
bmi = int(result) #this is an int so will return a whole number only 
print(bmi) 

#make the bmi int a str so it can be concatenated with a string of text.

bmi_as_str = str(bmi)#this is a string so can be concatenated, we keep the original bmi variable so it can be reused if needed
print("your bmi is "+bmi_as_str) 

#we can also convert the bmi int into a str in one line:
bmi = str(int(result)) #this overwrites the original variable converting it from an int into a str, we can no longer perform mathematical operations on this variable but we can use it as a string:
print("Your Body Mass Index is " + bmi) 

if result <18.5:
  print(f"Your BMI is {result}, you are underweight.")
elif result <25:
  print(f"Your BMI is {result}, you have a normal weight.")
elif result <30:
  print(f"Your BMI is {result}, you are slightly overweight.")
elif result <35:
  print(f"Your BMI is {result}, you are obese.")
else:
  print(f"Your BMI is {result}, you are clinically obese")

