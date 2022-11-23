from ControllerBar import ControllerBar
from OrderModel import Order

controller = ControllerBar()
numOrder = 0

'''METODO PARA ANYADIR PRODUCTOS A UN PEDIDO QUE YA EXISTE
   LO USAMOS EN LA OPCION 4 DEL MENU'''
def addProductsToExistingOrder(numProducts,order):
    while(True):
        #nameProduct = NOMBRE DE PRODUCTO
        nameProduct = input("Enter a PRODUCT NAME (END to finish): ")
        #SI EL nameProduct ES END, SE ACABA EL BUCLE
        if(nameProduct == "END"):
            break
        #product =  OBJETO PRODUCTO CON TAL NOMBRE
        product = controller.getProductByName(nameProduct)
        #SI product ESTA VACIO, NO EXISTE
        if (product == None):
            print("This product doesn't exist!")
            break
        '''AHORA, SI ESE PRODUCTO YA EXISTE EN EL PEDIDO, SU 'ID'
           SERA SU CORRESPONDIENTE
           SINO, SERA UN NUMERO MAS DEL ULTIMO ID DE PRODUCTOS
        '''
        obtainedNumProduct = order.getNumOfProductByName(product.getName())
        if(obtainedNumProduct == None):
            numProducts += 1
            quantity = int(input("Enter the QUANTITY of the product: "))
            if (order.addNewProduct(numProducts,product,quantity)) == True:
                print("New product added")
            else:
                print("Product not added")
        else:
            quantity = int(input("Enter the new QUANTITY for the product: "))
            if (order.changeQuantityForAProductByName(product.getName(),quantity)) == True:
                print("Product updated")
            else:
                print("Error. Product not updated")


'''METODO PARA ANYADIR PRODUCTOS A UN PEDIDO QUE ESTAMOS CREANDO AHORA
LO USAMOS EN LA OPCION 2 DEL MENU'''
def addProductsToNewOrder():
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
        listProducts = addProductsToNewOrder()
        if(listProducts != None):
            print("Creating the order...")
            numOrder += 1
            newOrder = Order(table,client,waiter,listProducts)
            controller.addOrder(numOrder,newOrder)
            print("Order added!")

    elif option == 3:
        #OBTENEMOS LOS PEDIDOS I LOS PRODUCTOS DE ESE PEDIDO
        orders = controller.getOrders()
        for num,order in orders.items():
            products = order.getProducts()
            print("Order ",num)
            print("\tTable ",order.getTable())
            print("\tClient ",order.getClient())
            print("\tWaiter ",order.getWaiter())
            print("\tProducts:")
            for numProduct,lista in products.items():
                print("\t\tProduct: ",lista[0].getName(),", Quantity: ",lista[1])
            print("\tTotal price €: {:.2f}".format(order.getPax()))

    elif option == 4:
        #OBTENEMOS TODOS LOS PEDIDOS
        orders = controller.getOrders()
        #SI NO HAY PEDIDOS, SACAMOS PRINT
        if (len(orders)) > 0:
            num = int(input("Enter the order num to change it:"))
            #COMPROBAMOS SI EL 'ID' DEL PEDIDO EXISTE
            if controller.existsOrder(num) == False:
                print("This order num doesn't exists!")
            else:
                #OBTENEMOS EL OBJETO PEDIDO SEGUN SU 'ID'
                order = controller.getOrderByNum(num)
                print("We have the following products: ")
                #OBTENEMOS Y MOSTRAMOS PRODUCTOS DE LA ORDEN
                products = order.getProducts()
                for product,quantity in products.values():
                    print("\t\tName: ",product.getName(),", quantity: ",quantity)
                print("What do you want to change?")
                print("1- Add product")
                print("2- Delete product")
                option = int(input("Select an option: "))
                if option == 1:
                    #OBTENEMOS EL ULTIMO NUMERO DE PRODUCTO QUE TENEMOS
                    numProducts = order.getNumOfProducts()
                    ''' 
                    LLAMAMOS AL METODO PARA ANYADIR PRODUCTO 
                    PASANDOLE :
                    -> EL NUMERO DE PRODUCTO OBTENIDO
                    -> LA ORDEN CON LA QUE ESTAMOS TRABAJANDO '''
                    addProductsToExistingOrder(numProducts,order)
                elif option == 2:
                    pname = input("What product do u want to remove?: ")
                    numProduct = order.getNumOfProductByName(pname)
                    if (order.removeProductByNum(numProduct) == True):
                        print("Product removed!")

        else:
            print("We don't have any order!")
