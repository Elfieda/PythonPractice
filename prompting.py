from sys import argv

#promting user for input

age = input("How old are you?")
height = input("How tall are you?")

print(f"So you are {age} old")
print(f"So you are {height} tall")

#parameters, unpacking, variables
first, second, third = argv

#Eprint("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#promting and passing
#script, user_name = argv

#print(f"hi {user_name}, I'm the {script} script")
