
#========The beginning of the class==========
class Shoe:
    # defining the attributes
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # defines the methods get_cost , get_quantity and __str__
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#=============Shoe list===========
# initialises an empty list for shoes
shoes = []

#==========Functions outside the class==============

def read_shoes_data(shoes):
    # open the file and skip the first line
    with open("inventory.txt", "r") as file:
        next(file)

        for line in file:
            # split the line by comma and strip each element to remove leading/trailing whitespaces
            data = [x.strip() for x in line.split(",")]
            country, code, product, cost, quantity = data

            # convert cost and quantity to integers
            cost = int(cost)
            quantity = int(quantity)

            # create a Shoes object and append it to shoe_list
            shoes.append(Shoe(country, code, product, cost, quantity))
    return shoes


def capture_shoes(shoe):
    # gathers user input for country, cost , product , code and quantity
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = int(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoes.append(Shoe(country, code, product, cost, quantity))

def view_all(shoes_data):
    for index, shoe in enumerate(shoes_data):
        print(f"{index + 1}. {shoe.country} {shoe.code} ({shoe.product}) - {shoe.quantity} pcs.")


def re_stock(shoes):
    # finds the shoe object with the lowest quantity
    lowest_quantity_shoe = None
    lowest_quantity = float("inf")
    for shoe in shoes:
        if shoe.quantity < lowest_quantity:
            lowest_quantity = shoe.quantity
            lowest_quantity_shoe = shoe
    # asks the user if they would like to re-stock the lowest quantity shoe
    if lowest_quantity_shoe:
        answer = input(f"Do you want to re-stock {lowest_quantity_shoe.product}? (y/n)")
        if answer.lower() == "y":
            quantity = int(input("Enter quantity to add: "))
            lowest_quantity_shoe.quantity += quantity

def search_shoe(code):
    # iterates over the list using the product code to return the shoe
    for shoe in shoes:
        if shoe.code == code:
            return shoe
    return None

def value_per_item(shoes):
    # calculates the total value for each item in the list using formula value = cost * quantity
    total_value = 0
    for shoe in shoes:
        value = shoe.cost * shoe.quantity
        total_value += value
        print(f"{shoe.product}: {value}")
    print(f"Total value: {total_value}")

def highest_qty(shoes):
    # iterates over list to find the product with the greatest quantity
    highest_qty_product = None
    highest_qty = 0
    for shoe in shoes:
        if shoe.quantity > highest_qty:
            highest_qty = shoe.quantity
            highest_qty_product = shoe
    if highest_qty_product:
        print(f"The product with the highest quantity is {highest_qty_product.product} with a quantity of {highest_qty}.")
    else:
        print("There are no shoes in the list.")

#==========Main Menu=============
# defines a main menu with numbered options for ease of use
def main():
    shoes_data = []
    while True:
        print("Welcome to the Shoe Inventory Management System")
        print("Please choose an option from the menu below:")
        print("1. Read data from file")
        print("2. Capture new shoe data")
        print("3. View all shoes")
        print("4. Restock shoes")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Determine highest quantity product")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            shoes_data = read_shoes_data(shoes)
        elif choice == "2":
            shoes_data.append(capture_shoes(shoes))
        elif choice == "3":
            view_all(shoes_data)
        elif choice == "4":
            re_stock(shoes_data)
        elif choice == "5":
            search_shoe(shoes_data)
        elif choice == "6":
            value_per_item(shoes_data)
        elif choice == "7":
            highest_qty(shoes_data)
        elif choice == "8":
            print("Thank you for using the Shoe Inventory Management System. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
