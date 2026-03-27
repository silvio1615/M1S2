inventory = []
def agregar_producto():
    name_producto = input("Ingrese el nombre del producto: ")

    val_cant = True
    while val_cant:
        try:
            quantity = int(input("Ingrese la cantidad: "))
            if quantity < 0:
                print("Error: ingrese un valor positivo.")
            else:
                val_cant = False
        except ValueError:
            print("Error: ingrese un número entero válido.")

    val_price = True
    while val_price:
        try:
            price = float(input("Ingrese el precio: "))
            if price < 0:
                print("Error: ingrese un valor positivo.")
            else:
                val_price = False
        except ValueError:
            print("Error: ingrese un número válido.")

    product = {
         "product":name_producto,
         "quantity":quantity,
         "price":price,
         "total_cost":price * quantity
    }
    inventory.append(product)
    return product
def mostrar_inventario():
    if not inventory                    :
        print ("no list recorded")
    else:
        print("list registred")
        for product in inventory:
         print(f"prodict:{product['product']}|quantity:{product['quantity']}|price{product['price']}|total cost:{product['total_cost']}")
def calcular_estadistica():
    if not inventory:
        print ("no list recorded")
    else:
        print ("calculate recorded")
        result = 0
        total_product=0 
        for product in inventory:
            total_product+=1
            result += product["price"] * product ["quantity"]
            print("\n--- ESTADÍSTICAS ---")
            print(f"Cantidad total de productos registrados: {total_product}")
            print(f"Valor total del inventario: ${result:.2f}")
def menu():
    print("\n--- MENÚ ---")
    print("1.agregar producto")
    print("2.mostrar inventario")
    print("3.ver estadistica")
    print("4.salir")

        
