# # Float → number with decimals
# temperature = 36.6

# # String → text, must be in quotes
# name = "Alice"

# print("Name:", name)           # Outputs: Name: Alice
# print("Temperature:", temperature)  # Outputs: Temperature: 36.6

# number = 5
# print(type(number))

# bottle = True
# print(type(bottle))

# shirt = 9.05
# print(type(shirt))

# phone = "Iphone"
# print(type(phone))

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# d = b

# #even if the value is the same, if we havent assigned it its not the same
# #with a is b we ask for true or false 
# # it can be true only if we assigned one variable to another 
# print(a is d)


# age=int(input("How old are you?: "))

# if age < 18:
#     print("You are a minor.")
# elif age < 13:
#     print("You are kid.")
# elif age == 18:
#     print("You are exactly 18.")
# else:
#     print("You are an adult.")


def age_calculator():
     age = int(input("How old are you?: "))

     if age < 18:
        print("You are a minor.")
     elif age < 13:
            print("You are kid.")
     elif age == 18:
        print("You are exactly 18.")
     else:
        print("You are an adult.")

age_calculator()

