# x = 5
# def print_local():
#     x = 5  # Local variable inside function
#     print("Inside function:", x)

# print_local()
# print("Outside function:", x) 

#!!!!!!!!

# Create an empty list to store our habits
habits = []  

def add_habit(habit_name):
    habits.append(habit_name)

habit_name = input("What is your habit? ")
add_habit("Drink water")    
add_habit("Exercise")   
add_habit(habit_name)    

print("Your habits:", habits)  






# modules #erros
try:   
    x = int(input("Enter a number: "))
    print("You entered:", x) 

except ValueError:
    print("That's not a valid number!")
#try and except you try something and it prints an error if it is not how it is supposed to be!

