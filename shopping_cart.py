items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yogurt']
prices = [40, 80, 120, 180, 60]
cart = []

print("Welcome to E-Kart Shopping!")
while True:
    print("\nMenu:")
    print("1: View available items")
    print("2: Add items to cart")
    print("3: Update item quantity in cart")
    print("4: Remove items from cart")
    print("5: Print the bill")
    print("6: Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Items:")
        for index, (item, price) in enumerate(zip(items, prices)):
            print(f"{index + 1}. {item} - Price: {price}")

    elif choice == 2:
        item_name = input("Enter the item name: ").capitalize()
        if item_name in items:
            quantity = int(input("Enter the quantity: "))
            for item in cart:
                if item[0] == item_name:
                    item[1] += quantity
                    print(f"Updated {item_name} quantity in the cart.")
                    break
            else:
                price = prices[items.index(item_name)]
                cart.append([item_name, quantity, price])
                print(f"Added {item_name} to the cart.")
        else:
            print("Item not found. Please choose an item from the available list.")

    elif choice == 3:
        item_name = input("Enter the item to update: ").capitalize()
        for item in cart:
            if item[0] == item_name:
                new_quantity = int(input("Enter the new quantity: "))
                item[1] = new_quantity
                print(f"Updated {item_name} quantity to {new_quantity}.")
                break
        else:
            print(f"{item_name} is not in the cart.")

    elif choice == 4:
        item_name = input("Enter the item to remove: ").capitalize()
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
                print(f"Removed {item_name} from the cart.")
                break
        else:
            print(f"{item_name} is not in the cart.")

    elif choice == 5:
        print("\nCart Details:")
        if not cart:
            print("Your cart is empty.")
        else:
            total_amount = 0
            for item in cart:
                name, quantity, price = item
                total = quantity * price
                total_amount += total
                print(f"{name}: Quantity: {quantity}, Price per item: {price}, Total: {total}")
            print(f"Total Amount: {total_amount}")

    elif choice == 6:
        print("Thank you for shopping with us! Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")
