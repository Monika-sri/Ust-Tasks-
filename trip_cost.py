distance = int(input("Enter the distance to drive in kilometers: "))
efficiency = int(input("Enter the car's fuel efficiency in kilometers per liter: "))
fuel_price = int(input("Enter the price per liter of fuel: "))

def calculate_trip_cost():
    fuel_needed = distance / efficiency
    total_cost = fuel_needed * fuel_price
    print("The total trip cost is:", total_cost)

calculate_trip_cost()
