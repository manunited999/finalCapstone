
#========The beginning of the class==========
# define a class called shoe, which is for all shoe objects
class Shoe:

# an initialiser which has the country, code, cost and quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# getters for each of the class attributes, so that they can be retrieved later on in the program
    def get_cost(self):
        return self.cost
    
    def get_code(self):
        return self.code

    def get_quantity(self):
        return self.quantity
    
    def get_product(self):
        return self.product

    def get_country(self):
        return self.country

    # A string method to print out the details of a specific shoe

    def __str__(self):
        return f"Country: {self.country}. Code: {self.code}. Product: {self.product}. Cost: {self.cost}. Quantity: {self.quantity}\n"



#=============Shoe list===========
# an empty shoe list
shoe_list = []

# read data from the inventory.txt file and then append them to the shoe list
def read_shoes_data(filename):
    try:
        with open(filename, "r") as shoe_data: 
            next(shoe_data)
            for line in shoe_data:
                split_line = line.strip().split(",")
# if statement to ensure that empty lines aren't added, which would break the code 
                if len(split_line) == 5:
                    country, code, product, cost, quantity = split_line
# each shoe in the list will be a class with the 5 attributes
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
        return shoe_list
# Error handling to ensure that the file is there
    except FileNotFoundError:
        print("\nError. File does not exist.")

# This function is designed to add a shoe to the list, and then write it to the file
def capture_shoes(filename):
# ask the user for input on the attributes of the shoe, adding error handling where appropriate
    country = input("Please enter the country: ")
    code = input("Please enter the product code: ")
    product = input("Please enter the product: ")
    try:
        cost = float(input("Please enter the cost: "))
    except ValueError:
        print("Invalid cost value. Cost should be a number.")
        return
    try:
        quantity = int(input("Please enter the quantity: "))
    except ValueError:
        print("Invalid quantity value. Quantity should be an integer.")
        return
# the shoe is an instance of the class Shoe
    shoe = Shoe(country, code, product, cost, quantity)
# add the shoe to the shoe list
    shoe_list.append(shoe)
# write the shoe to the file
    try:
        with open(filename, "a") as file:
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
    except FileNotFoundError:
        print("Error. File does not exist.")

# function for viewing all shoes
def view_all():
# print all shoes in the shoe list, which will print using the string method
    for shoe in shoe_list:
        print("-" * 100)
        print(shoe)



def re_stock(filename):
    # Find the shoe with the lowest quantity
    lowest_quantity = 0
    shoe_to_restock = None
    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity:
            lowest_quantity = shoe.get_quantity()
            shoe_to_restock = shoe

    # Ask the user if they want to re-stock the shoe, only if the shoe is in the list
    if shoe_to_restock is not None:
        # prompt the user for input on the shoe
        response = input(f"Do you want to re-stock the {shoe_to_restock.product}? (Yes or No) ")
        # if yes
        if response.upper() == "Yes":
        # then enter the quantity to add
            try:
                quantity = int(input("Enter the quantity to add: "))
                shoe_to_restock.quantity += quantity
            except ValueError:
                print("Error, please enter a valid number.")

            # Update the quantity of that shoe in the file, once it is restocked as the user has added
            try:
                with open(filename, "r") as shoe_data:
                    lines = shoe_data.readlines()
                for i, line in enumerate(lines):
                    if line.startswith(f"{shoe_to_restock.country},{shoe_to_restock.code}"):
                        line_list = line.strip().split(",")
                        line_list[-1] = str(shoe_to_restock.quantity)
                        lines[i] = ",".join(line_list) + "\n"
            except FileNotFoundError:
                print("Error, the file does not exist.")
            try:
                with open(filename, "w") as shoe_data:
                    shoe_data.writelines(lines)
            except FileNotFoundError:
                print("Error, the file does not exist.")


# Function to find a shoe
def search_shoe():
# enter the cose
    requested_code = input("Enter the shoe code to search: ")
# set a boolean value to False to signify if the shoe has been found
    found = False
    for shoe in shoe_list:
# for each shoe in the shoe list
        if shoe.get_code() == requested_code:
# if the code input by the user matches the code in the line
# print the code and turn to found
            print(f"\n{shoe}\n")
            found = True
            break
# if the code doesn't match any in the file, then state shoe not found
    if not found:
        print("\nError. Shoe not found\n")


def value_per_item():
    # for each shoe in the shoe list
    for shoe in shoe_list:
    # the value of the shoe multiplied by the quantity of the shoe, which we get from the class definition
        shoe_value = shoe.get_cost() * shoe.get_quantity()
# print out the details of the code, product and overall value
        print(f"Shoe Code: {shoe.code}, Product: {shoe.product}, Value: {shoe_value}")
    

def highest_quantity():
    high_quantity_shoe = None
    high_quantity = 0
    for shoe in shoe_list:
        if shoe.quantity > high_quantity:
            high_quantity = shoe.quantity
            high_quantity_shoe = shoe
    if high_quantity_shoe:
        print(f"{high_quantity_shoe.product} is for sale, with the highest quantity of {high_quantity}")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Please enter the path of the inventory.txt file here
filename = "/Users/eso/Desktop/HyperionDev/L30/inventory.txt"

# main running of the program, when the program is run the options will display which the user will choose
while True:
    print("Welcome to the Shoe Store")
    print("Select an option:")
    print("1. Display all shoes")
    print("2. Search for a shoe by SKU")
    print("3. Add a new shoe")
    print("4. Restock a shoe")
    print("5. Display value of each shoe")
    print("6. Display the highest quantity shoe")
    print("7. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        shoe_list = read_shoes_data(filename)
        view_all()
    elif choice == 2:
        shoe_list = read_shoes_data(filename)
        search_shoe()
    elif choice == 3:
        shoe_list = read_shoes_data(filename)
        capture_shoes(filename)
    elif choice == 4:
        shoe_list = read_shoes_data(filename)
        re_stock(filename)
    elif choice == 5:
        shoe_list = read_shoes_data(filename)
        value_per_item()
    elif choice == 6:
        shoe_list = read_shoes_data(filename)
        highest_quantity()
    elif choice == 7:
        print("Thank you for using the Shoe Store. Have a great day!")
        break
    else: 
        print("Invalid Option, Please Enter Again.")

