items = [
    {"name": "Bread", "price": 40},
    {"name": "Cookies", "price": 80},
    {"name": "Butter", "price": 120},
    {"name": "Cheese", "price": 180},
    {"name": "Yoghurt", "price": 60}
]

cart = []

def view_items():
    print("Available items:")
    for item in items:
        print(f"Name: {item['name']} Price: {item['price']}")

def add_to_cart():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    for item in items:
        if item['name'].lower() == item_name.lower():
            cart.append({"name": item['name'], "quantity": quantity, "price": item['price'], "total": quantity * item['price']})
            print(f"Added {quantity} of {item['name']} to the cart.")
            return
    print("Item not found!")

def update_cart():
    item_name = input("Which item to be updated: ")
    quantity = int(input("Enter the quantity to be updated: "))
    for item in cart:
        if item['name'].lower() == item_name.lower():
            item['quantity'] = quantity
            item['total'] = quantity * item['price']
            print(f"Updated {item['name']} to quantity {quantity}.")
            return
    print("Item not found in the cart!")

def delete_from_cart():
    item_name = input("Which item to be removed: ")
    for item in cart:
        if item['name'].lower() == item_name.lower():
            cart.remove(item)
            print(f"Removed {item['name']} from the cart.")
            return
    print("Item not found in the cart!")

def print_bill():
    print("\nCart Items:")
    print("Name, Quantity, Price, Total")
    total_amount = 0
    for item in cart:
        print(f"{item['name']}, {item['quantity']}, {item['price']}, {item['total']}")
        total_amount += item['total']
    print(f"Total Amount of Bill: {total_amount}\n")

def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. View Items")
        print("2. Add Items to Cart")
        print("3. Update Items in Cart")
        print("4. Delete Items from Cart")
        print("5. Print Bill")
        print("6. Exit")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            view_items()
        elif choice == 2:
            add_to_cart()
        elif choice == 3:
            update_cart()
        elif choice == 4:
            delete_from_cart()
        elif choice == 5:
            print_bill()
        elif choice == 6:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
