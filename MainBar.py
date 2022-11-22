from ControllerBar import ControllerBar
from OrderModel import Order

controller = ControllerBar()
numOrder = 0

def addProductstoOrder2(numProducts,order):
    while(True):
        pname = input("Enter a PRODUCT NAME (END to finish): ")
        if(pname == "END"):
            break
        product = controller.getProductByName(pname)
        if (product == None):
            print("This product doesn't exist!")
            break
        numProducts += 1
        quantity = int(input("Enter the QUANTITY of the product: "))
        if (order.addNewProduct(numProducts,product,quantity)) == True:
            print("New product added")
        else:
            print("Product not added")

def addProductstoOrder():
    listProducts = {}
    numProduct = 0
    while(True):
        pname = input("Enter a PRODUCT NAME (END to finish): ")
        if(pname == "END"):
            break
        product = controller.getProductByName(pname)
        if (product == None):
            print("This product doesn't exist!")
            break
        numProduct += 1
        quantity = int(input("Enter the QUANTITY of the product: "))
        listProducts[numProduct] = [product,quantity]
    if (len(listProducts)) > 0: 
        return listProducts
    else:
        return None

while(True):
    print()
    print("We have ",controller.getNumCategories()," categories")
    print("We have ",controller.getNumProducts()," products")
    #print("We have ",controller.getNumIngredients()," ingredients")
    print()
    print("1- List menu")
    print("2- Create order")
    print("3- List orders")
    print("4- Change a order")
    print("0- Exit")
    option = int(input("Select an option: "))

    if (option == 0):
        print("BYE!")
        break

    #LIST CATEGORIES
    elif option == 1:
        listCategories = controller.getCategories()
        for idd,cat in listCategories.items():
            print("Category ",idd)
            print("\t",cat.getName())
            print("\t","Products: ")
            for idProducto in cat.getProducts():
                producto = controller.getProductById(idProducto)
                print("\t\t",producto.getName())

    elif option == 2:
        table = input("Enter the table num: ")
        client = input("Enter the client name: ")
        waiter = input("Enter the waiter name: ")
        listProducts = addProductstoOrder()
        if(listProducts != None):
            print("Creating the order...")
            numOrder += 1
            newOrder = Order(table,client,waiter,listProducts)
            controller.addOrder(numOrder,newOrder)
            print("Order added!")

    elif option == 3:
        orders = controller.getOrders()
        for num,order in orders.items():
            print("Order ",num)
            print("\tTable ",order.getTable())
            print("\tClient ",order.getClient())
            print("\tWaiter ",order.getWaiter())
            print("\tProducts:")
            order.printProducts()
            print("\tTotal price €: {:.2f}".format(order.getPax()))

    elif option == 4:
        orders = controller.getOrders()
        if (len(orders)) > 0:
            num = int(input("Enter the order num to change it:"))
            if controller.existsOrder(num) == False:
                print("This order num doesn't exists!")
            else:
                order = controller.getOrderByNum(num)
                print("We have the following products: ")
                order.printProducts()
                print("What do you want to change?")
                print("1- Add product")
                print("2- Delete product")
                option = int(input("Select an option: "))
                if option == 1:
                    numProducts = order.getNumOfProducts()
                    newProducts = addProductstoOrder2(numProducts,order)
                elif option == 2:
                    pname = input("What product do u want to remove?: ")
                    numProduct = order.getNumOfProductByName(pname)
                    if (order.removeProductByNum(numProduct) == True):
                        print("Product removed!")

        else:
            print("We don't have any order!")
