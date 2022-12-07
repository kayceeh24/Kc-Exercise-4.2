# Programmer: KC
# Helped By: 

# Function for printing multiplication facts for a number
num_1 = int(input("Enter an integer: "))
num_2 = int(input("How many facts do you want? "))
print("")
for x in range(num_2):
    print(x + 1, "X", num_1, "=", (x + 1) * num_1)
