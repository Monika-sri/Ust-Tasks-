# Input the quantity and price per item
quantity = int(input("Enter the quantity purchased: "))
price_per_item = float(input("Enter the price per item: "))

# Calculate total price before discount
total_price_before_discount = quantity * price_per_item

# Check if discount is applicable
if quantity > 10:
    discount = 0.10 * total_price_before_discount  # 10% discount
    total_price_after_discount = total_price_before_discount - discount  # Apply discount
else:
    total_price_after_discount = total_price_before_discount  # No discount if quantity is 10 or less

# Display the result
print(f"Total price before discount: ${total_price_before_discount:.2f}")
print(f"Total price after discount: ${total_price_after_discount:.2f}")
