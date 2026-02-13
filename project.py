import math 
#Write a Python program that Asks the user to enter a number, displays whether the number is If the number is positive, also display whether it is
def number_checker():
    user =  math.floor(float(input ("Enter a number: ")))
    #user = round(user, 0)
    #user = math.ceil(user)
    #user = math.floor(user)



    if user  % 2 == 0 :
        print("Your number is even ")

    else:
        print("Your number is odd")

    if user >= 0: 
        print(f"Your number {user}, it positive")

    else:
        print(f"Your number is {user} is negative")

number_checker()


# Create a program that: Repeatedly asks the user to enter a password, the program should only stop when the
#  correct password "BTEC2026" is entered and display how many attempts the user made.

def password_guess():   
    password = "BTEC2026"
    while True:
        user_input = input("Enter password to guess: ") 
        if user_input == password:
            print(F"You got the correct passord: {password}")
            break 
        else:
            print(f"Wrong, correct password is {password}")



#Write a function called calculate_average() that:
#Accepts a list of numbers as a parameter.
#Returns the average of the numbers.
#In the main program, allow the user to enter 5 numbers and store them in a list.
#Call the function and display the result.

def calculate_average():
    numbers = []
    for i in range(5):
        user = int(input(f" {1+i} Enter a number: "))
        numbers.append(user)

    average = sum(numbers) / len(numbers)
    print (f"Your average is: {average}")



# Create a program to manage student grades:
#Store 3 students’ names and their grades in a dictionary.
#Allow the user to search for a student by name.
#Display the student’s grade or show an error message if the name is not found.

def grade_checker(): 
    dict = {"Milo": 80,
            "Abdul": 70,
            "Warren": 5}

    user = input("Enter Your name: ").capitalize().strip()
    grade = dict.get(user)

    if grade is not None:
        print(f"{user} garde is: {grade}")

    else:
        print("Your name doesnt exit")