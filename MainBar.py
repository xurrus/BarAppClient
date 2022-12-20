from ControllerBar import ControllerBar
from OrderModel import Order
from ApiBar import ApiBar

from IngredientModel import Ingredient
from CategoryModel import Category
from ProductModel import Product

controller = ControllerBar()
api = ApiBar()
numOrder = 0 #CONTADOR PARA ACADA COMANDA QUE SE CREA EN LA APLICACION

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
    # print("We have ",controller.getNumCategories()," categories")
    # print("We have ",controller.getNumProducts()," products")
    # print("We have ",controller.getNumIngredients()," ingredients")
    # print()
    print("1. List menu")
    print("2. Create order")
    print("3. List orders")
    print("4. Change a order")
    print("0. Exit")
    print("- - - - - - - - -")
    print("5- C.R.U.D Menu")
    option = int(input("Select an option: "))

    #EXIT
    if (option == 0):
        print("BYE!")
        break

    #LIST CATEGORIES AND THEIR PRODUCTS
    elif option == 1:
        listCategories = controller.getCategories()
        for idd,cat in listCategories.items():
            print("Category ",idd)
            print("\t",cat.getName())
            print("\t","Products: ")
            for idProducto in cat.getProducts():
                producto = controller.getProductById(idProducto)
                print("\t\t",producto.getName())
    #CREATE ORDER
    elif option == 2:
        table = input("Enter the table num: ")
        client = input("Enter the client name: ")
        waiter = input("Enter the waiter name: ")
        listProducts = addProductsToNewOrder()
        #listProducts[contadorProducto] = [producto,cantidad]
        if(listProducts != None):
            print("Creating the order...")
            numOrder += 1 #HEMOS CREADO UNA ORDEN; ENTONCES INCREMENTAMOS CONTADOR
            newOrder = Order(table,client,waiter,listProducts)
            controller.addOrder(numOrder,newOrder)
            #orders[numOrder] = newOrder
            print("Order added!")

    elif option == 3:
        #OBTENEMOS LOS PEDIDOS I LOS PRODUCTOS DE ESE PEDIDO
        #orders[numOrder] = newOrder
        orders = controller.getOrders()
        for num,order in orders.items():
            products = order.getProducts() #OBTENEMOS LOS PRODUCTOS DE CADA ORDEN
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
    #CRUD MENU
    elif option == 5:
        while(True):
            print("1- INGREDIENTS Management")
            print("2- CATEGORIES Management")
            print("3- PRODUCTS Management")
            print("0- Exit")
            opCRUD = int(input("Select an option: "))

            if opCRUD == 0:
                break

            #INGREDIENT CRUD
            elif opCRUD == 1:
                while(True):
                    print("C) Create a new ingredient")
                    print("R) Read ingredients")
                    print("U) Update an ingredient")
                    print("D) Delete an ingredient")
                    print("0) Exit")
                    opI = input("Select an option:")

                    if opI == '0':
                        break
                    
                    elif opI == 'C':
                        name = input("Name for the new ingredient: ")
                        print("Possible types of ingredients:")
                        print("Fats and oils | Eggs or Milk | Fruits | Vegetables | Grain, nuts")
                        print("Herbs and spices | Meat | Fish | Pasta | Others")
                        typeI = input("Choose the type for the new ingredient: ")
                        observations = input("Observations: ")
                        print("We have the following products:")
                        allProducts = controller._getProducts()
                        for id,prod in allProducts.items():
                            print(id,"-",prod.getName())
                        prodIds = []
                        while(True):
                            prodId = int(input("Enter the ID of the product that contains this ingredient (0 to end):"))
                            if prodId == 0:
                                break
                            else:
                                prodIds.append(prodId)
                        newIngredient = Ingredient(None,name,typeI,observations,prodIds)
                        if controller._addIngredient(newIngredient):
                            print("New ingredient added with id ",newIngredient.getId())
                        else:
                            print("Error. Not added")

                    elif opI == 'R':
                        while(True):
                            print("1- Read one ingredient by ID")
                            print("2- Read all ingredients")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            if opRead == 1:
                                idd = input("Enter the ingredient ID:")
                                ingredient = controller._getIngredientById(idd)
                                if ingredient == None:
                                    print("This ingredient doesn't exists")
                                    break
                                print("Ingredient ",ingredient.toString())

                            elif opRead == 2:
                                allIngredients = controller._getIngredients()
                                print("Ingredients:")
                                for id,ing in allIngredients.items():
                                    print(ing.toString())

                            elif opRead == 0:
                                break

                    elif opI == 'U':
                        idd = input("Enter the ingredient to update (his ID):")
                        ingredient = controller._getIngredientById(idd)
                        if ingredient == None:
                            print("This ingredient doesn't exists")
                        else:
                            while(True):
                                print("What param do you want to update?:")
                                print("1- Name ",ingredient.getName())
                                print("2- TypeI ",ingredient.getTypeI())
                                print("3- Observations ",ingredient.getObservations())
                                print("4- Products ",ingredient.getProducts())
                                print("5- Update")
                                print("0- Exit")
                                opParam = int(input("Choose a param: "))
                                if opParam == 1:
                                    name = input("Enter the new name: ")
                                    ingredient.setName(name)

                                elif opParam == 2:
                                    print("Possible types of ingredients:")
                                    print("Fats and oils | Eggs or Milk | Fruits | Vegetables | Grain, nuts")
                                    print("Herbs and spices | Meat | Fish | Pasta | Others")
                                    typeI = input("Choose the type for the new ingredient: ")
                                    ingredient.setTypeI(typeI)

                                elif opParam == 3:
                                    observations = input("Enter the new observations: ")
                                    ingredient.setObservatons(observations)
                                
                                elif opParam == 4:
                                    print("We have the following products:")
                                    allProducts = controller._getProducts()
                                    for id,prod in allProducts.items():
                                        print(id,"-",prod.getName())
                                    prodIds = []
                                    while(True):
                                        prodId = int(input("Enter the ID of the product that contains this ingredient (0 to end):"))
                                        if prodId == 0:
                                            break
                                        else:
                                            prodIds.append(prodId)
                                    ingredient.setProducts(prodIds)

                                elif opParam == 5:
                                    if controller._updateIngredient(ingredient):
                                        print("Ingredientt updated")
                                    else:
                                        print("ERROR. Not updated")

                                elif opParam == 0:
                                    break

                    elif opI == 'D':
                        allIngredients = controller._getIngredients()
                        print("Ingredients:")
                        for id,ing in allIngredients.items():
                            print(id," ",ing.getName())
                        idd = input("Enter the ingredient ID to remove:")
                        ingredient = controller._getIngredientById(idd)
                        if ingredient == None:
                            print("Error. This ingredient doesn't exists")
                        else:
                            if controller._deleteIngredient(idd):
                                print("Ingredient removed")
                            else:
                                print("ERROR. Not removed")

            
            #CATEGORY CRUD
            elif opCRUD == 2:
                while(True):
                    print("C) Create a new category")
                    print("R) Read categories")
                    print("U) Update a category")
                    print("D) Delete a category")
                    print("0) Exit")
                    opC = input("Select an option")

                    if opC == '0':
                        break
                    
                    elif opC == 'C':
                        pass

                    elif opC == 'R':
                        pass

                    elif opC == 'U':
                        pass
                    
                    elif opC == 'D':
                        pass

            #PRODUCT CRUD
            elif opCRUD == 3:
                while(True):
                    print("C) Create a new product")
                    print("R) Read products")
                    print("U) Update a product")
                    print("D) Delete a product")
                    print("0) Exit")
                    opP = input("Select an option")

                    if opP == '0':
                        break
                    
                    elif opP == 'C':
                        pass

                    elif opP == 'R':
                        pass

                    elif opP == 'U':
                        pass
                    
                    elif opP == 'D':
                        pass
            

    
