

#Ask the user to input their name using the input() function, then store their name in the variable 'name'.
name = input("Please enter your name: ")

#Ask the user to input their age using the input() function, then store their age in the variable 'age'.
age = int(input("Please enter your age: "))

#Ask the user to input their house number using the input() function, then store their name in the variable 'houseNum'.
houseNum = input("Please enter your house number: ")

#Ask the user to input their street name using the input() function, then store their name in the variable 'streetName'.
streetName = input("Please enter your street name: ")

#Use the f-string to print a full sentence containing all the details of the user to the screen.
print(f"This is {name}. He is {age} years old and lives at house number {houseNum} on {streetName}.")
