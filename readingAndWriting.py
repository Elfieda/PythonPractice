from sys import argv
script, filename = argv
print(f"We'r going to erase {filename}")
print("If you dont want that, hit CTRL-C")
print("If you do want that,hit return")

input("?")
print("Opening the file..")
target = open(filename, 'w')

print("Truncating the fike. GoodBye")
target.truncate()

print("Now I'm going to ask you for the three lines.")

line1 = input("line 1: ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("Im going to write these lines to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally, we close it")
target.close()