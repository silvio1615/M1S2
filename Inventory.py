# Global list that stores all inventory products
inventory = []

def add_product():
    # Ask the user for the product name
    product_name = input("Enter the product name: ")

    # --- Quantity validation ---
    valid_quantity = True
    while valid_quantity:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("Error: please enter a positive value.")
            else:
                valid_quantity = False  # Exit loop if value is valid
        except ValueError:
            print("Error: please enter a valid integer.")

    # --- Price validation ---
    valid_price = True
    while valid_price:
        try:
            price = float(input("Enter the price: "))
            if price < 0:
                print("Error: please enter a positive value.")
            else:
                valid_price = False  # Exit loop if value is valid
        except ValueError:
            print("Error: please enter a valid number.")

    # Build the product dictionary with its data
    product = {
        "product": product_name,
        "quantity": quantity,
        "price": price,
        "total_cost": price * quantity  # Total cost = price × quantity
    }

    # Add the product to the global list
    inventory.append(product)
    return product


def show_inventory():
    # Check if the inventory is empty
    if not inventory:
        print("No products recorded.")
    else:
        print("Registered products:")
        # Iterate and print each product
        for product in inventory:
            print(f"Product: {product['product']} | Quantity: {product['quantity']} | Price: {product['price']} | Total cost: {product['total_cost']}")


def calculate_statistics():
    # Check if the inventory is empty
    if not inventory:
        print("No products recorded.")
    else:
        print("Calculating statistics...")
        result = 0        # Accumulator for the total inventory value
        total_products = 0  # Product counter

        for product in inventory:
            total_products += 1
            result += product["price"] * product["quantity"]

        # Print final totals after the loop finishes
        print("\n--- STATISTICS ---")
        print(f"Total products registered: {total_products}")
        print(f"Total inventory value: ${result:.2f}")


def menu():
    # Display the main menu options
    print("\n--- MENU ---")
    print("1. Add product")
    print("2. Show inventory")
    print("3. View statistics")
    print("4. Exit")
