#Data types

#String

#print certain index of a string (subscripting)
print("Hello"[2])

#concatenation
print("123"+"456")

# integer

print(123+456) #returns the sum of these integers.

print(123_465_789) # underscores will be removed.

#float - any number that has a decimal place:

print(3.14159)

#Boolean - True/False

True
False

# type
length = len("craig")
print(length)
print(type(length))

#type casting

#this will break the code as we cannot concatenate integers and strings. 
#the int needs to be converted into a string first.

        # print("your name has " + length + " characters")

#convert the integer 'length' into a string.
length_to_string = str(length) 

#now we can run the line above, using the new variable(length_to_string):

print("your name has " + length_to_string + " characters")




#rounding numbers

#use the round() function to round to the nearest whole number:
print(round(8/3))

##use the floor operator to round down to the nearest whole number:

print(round(8//3))

#round the equation to x decimal places:
print(round(8/3,2))

#round a number to x decimal places
print(round(2.675425625,2))









