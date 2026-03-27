# Import all functions from the inventory module
from inventory import add_product, show_inventory, calculate_statistics, menu

# Flag to keep the main loop running
running = True

while running:
    # Display the menu options
    menu()
    option = input("Select an option: ")

    if option == "1":
        # Add a new product to the inventory
        add_product()
    elif option == "2":
        # Display all registered products
        show_inventory()
    elif option == "3":
        # Show inventory statistics
        calculate_statistics()
    elif option == "4":
        # Exit the program
        print("Exiting the program.")
        break
    else:
        # Handle invalid input
        print("Invalid option. Please try again.")
