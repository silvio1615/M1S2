inventory = []

def agregar_producto():
    name_producto = input("Ingrese el nombre del producto: ")
    quantity = int(input("Ingrese la cantidad: "))
    price = float(input("Ingrese el precio: "))
    total_cost=0
    list = {
         "product":name_producto,
         "quantity":quantity,
         "price":price,
         "total cost":total_cost
    }
    inventory.append(list)
    return list
def mostrar_inventario(inventory):
    if not inventory                    :
        print ("no list recorded")
    else:
        print("list registred")
        for list in inventory:
         print(f"prodict:{list['product']},|quantity:{list['quantity']},|price{list['price']},total cost:{list['total_cost']}")
def calcular_estadistica(inventory,):
   total_cost= inventory["price"] * inventory["quantity"]
   
