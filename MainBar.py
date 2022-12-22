from ControllerBar import ControllerBar
from OrderModel import Order

from IngredientModel import Ingredient
from CategoryModel import Category
from ProductModel import Product

controller = ControllerBar()

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

def printAllIngredients():
    allIngredients = controller._getIngredients()
    print("Ingredients:")
    for id,ing in allIngredients.items():
        print("\tID ",id," - ",ing.getName()," Type: ",str(ing.getTypeI()))
        print()

def printAllCategories():
    allCategories = controller._getCategories()
    print("Categories:")
    for id,cat in allCategories.items():
        print("\tID ",id," - ",cat.getName())
        print()

def printAllProducts():
    allProducts = controller._getProducts()
    print("Products:")
    for id,pro in allProducts.items():
        if pro.getCategory() == False:
            nameCat = "no category"
        else:
            nameCat = pro.getCategory()[1]
        print("\tID ",id," - ",pro.getName()," Category: ",nameCat,", Price: ",pro.getPrice(),"€")
        print()

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
            print()
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
                    print()
                    print("C) Create a new ingredient")
                    print("R) Read ingredients")
                    print("U) Update an ingredient")
                    print("D) Delete an ingredient")
                    print("0) Exit")
                    opI = input("Select an option: ")
                    print()

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
                            print("\tNew ingredient added with id ",newIngredient.getId())
                        else:
                            print("\tError. Not added")

                    elif opI == 'R':
                        while(True):
                            print("1- Read one ingredient by ID")
                            print("2- Read all ingredients")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            print()
                            if opRead == 1:
                                idd = input("Enter the ingredient ID:")
                                ingredient = controller._getIngredientById(idd)
                                if ingredient == None:
                                    print("\tERROR. THIS ID NOT EXISTS")
                                    break
                                productos = ingredient.getProducts()
                                if len(productos) > 0:
                                    message = "\tID - "+str(ingredient.getId())+"\n\tName: "+str(ingredient.getName())+"\n\tObservations: "+str(ingredient.getObservations())+"\n\tProducts:\n\t\t"
                                    for p in productos:
                                        message += str(controller._getProductById(p).getName())+" | "
                                    print(message)
                                    print()
                                else:
                                    message = "\tID - "+str(ingredient.getId())+"\n\tName: "+str(ingredient.getName())+"\n\tObservations: "+str(ingredient.getObservations())+"\n\tNo products"
                                    print(message)
                                    print()

                            elif opRead == 2:
                                printAllIngredients()

                            elif opRead == 0:
                                break

                    elif opI == 'U':
                        printAllIngredients()
                        idd = input("Enter the ingredient to update (his ID):")
                        ingredient = controller._getIngredientById(idd)
                        if ingredient == None:
                            print("\tThis ingredient doesn't exists")
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
                                        print("\t",id,"-",prod.getName())
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
                                        print("\tIngredient updated")
                                        break
                                    else:
                                        print("\tERROR. Not updated")

                                elif opParam == 0:
                                    break

                    elif opI == 'D':
                        printAllIngredients()
                        idd = input("Enter the ingredient ID to remove:")
                        ingredient = controller._getIngredientById(idd)
                        if ingredient == None:
                            print("\tError. This ingredient doesn't exists")
                        else:
                            if controller._deleteIngredient(idd):
                                print("\tIngredient removed")
                            else:
                                print("\tERROR. Not removed")

            
            #CATEGORY CRUD
            elif opCRUD == 2:
                while(True):
                    print()
                    print("C) Create a new category")
                    print("R) Read categories")
                    print("U) Update a category")
                    print("D) Delete a category")
                    print("0) Exit")
                    opC = input("Select an option: ")
                    print()

                    if opC == '0':
                        break
                    
                    elif opC == 'C':
                        name = input("Name for the new category: ")
                        print("We have the following products:")
                        allProducts = controller._getProducts()
                        for id,prod in allProducts.items():
                            print("\t",id,"-",prod.getName())
                        prodIds = []
                        while(True):
                            prodId = int(input("Enter the ID of the product belonging to this category (0 to end):"))
                            if prodId == 0:
                                break
                            else:
                                prodIds.append(prodId)
                        newCategory = Category(None,name,prodIds)
                        if controller._addCategory(newCategory):
                            print("\tNew category added with id ",newCategory.getId())
                        else:
                            print("\tError. Not added")

                    elif opC == 'R':
                        while(True):
                            print("1- Read one category by ID")
                            print("2- Read all categories")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            if opRead == 1:
                                idd = input("Enter the category ID:")
                                category = controller._getCategoryById(idd)
                                if category == None:
                                    print("\tTHIS CATEGORY DOESN'T EXISTS")
                                    break
                                productos = category.getProducts()
                                if len(productos) > 0:
                                    message = "\tID - "+str(category.getId())+"\n\tName: "+str(category.getName())+"\n\tProducts:\n\t\t"
                                    for p in productos:
                                        message += str(controller._getProductById(p).getName())+" | "
                                    print(message)
                                    print()
                                else:
                                    message = "\tID - "+str(category.getId())+"\n\tName: "+str(category.getName())+"\n\tNo products"
                                    print(message)
                                    print()

                            elif opRead == 2:
                                printAllCategories()

                            elif opRead == 0:
                                break

                    elif opC == 'U':
                        printAllCategories()
                        idd = input("Enter the category to update (his ID):")
                        category = controller._getCategoryById(idd)
                        if category == None:
                            print("\tThis category doesn't exists")
                        else:
                            while(True):
                                print("What param do you want to update?:")
                                print("1- Name ",category.getName())
                                print("2- Products ",category.getProducts())
                                print("3- Update")
                                print("0- Exit")
                                opParam = int(input("Choose a param: "))
                                if opParam == 1:
                                    name = input("Enter the new name: ")
                                    category.setName(name)
                                
                                elif opParam == 2:
                                    print("We have the following products:")
                                    allProducts = controller._getProducts()
                                    for id,prod in allProducts.items():
                                        print("\t",id,"-",prod.getName())
                                    prodIds = []
                                    while(True):
                                        prodId = int(input("Enter the ID of the product inside this category (0 to end):"))
                                        if prodId == 0:
                                            break
                                        else:
                                            prodIds.append(prodId)
                                    category.setProducts(prodIds)

                                elif opParam == 3:
                                    if controller._updateCategory(category):
                                        print("\tCategory updated")
                                        break
                                    else:
                                        print("\tERROR. Not updated")

                                elif opParam == 0:
                                    break
                    
                    elif opC == 'D':
                        printAllCategories()
                        idd = input("Enter the category ID to remove:")
                        category = controller._getCategoryById(idd)
                        if category == None:
                            print("\tError. This category doesn't exists")
                        else:
                            if controller._deleteCategory(idd):
                                print("\tCategory removed")
                            else:
                                print("\tERROR. Not removed")

            #PRODUCT CRUD
            elif opCRUD == 3:
                while(True):
                    print()
                    print("C) Create a new product")
                    print("R) Read products")
                    print("U) Update a product")
                    print("D) Delete a product")
                    print("0) Exit")
                    opP = input("Select an option: ")

                    if opP == '0':
                        break
                    
                    elif opP == 'C':
                        name = input("Name for the new product: ")
                        price = float(input("Price €: "))
                        description = input("Description: ")
                        print("We have the following categories:")
                        allCategories = controller._getCategories()
                        for id,cat in allCategories.items():
                            print("\t",id,"-",cat.getName())
                        catId = int(input("Enter the ID of the father category for this product: "))
                        print("We have the following ingredients")
                        allIngredients = controller._getIngredients()
                        for id,ing in allIngredients.items():
                            print("\t",id,"-",ing.getName())
                        ingIds = []
                        while(True):
                            ingId = int(input("Enter the ID of the ingredient that makes up this product (0 to end):"))
                            if ingId == 0:
                                break
                            else:
                                ingIds.append(ingId)

                        newProduct = Product(None,name,description,price,catId,ingIds)
                        if controller._addProduct(newProduct):
                            print("\tNew product added with id ",newProduct.getId())
                        else:
                            print("\tError. Not added")

                    elif opP == 'R':
                        while(True):
                            print("1- Read one product by ID")
                            print("2- Read all products")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            if opRead == 1:
                                idd = input("Enter the product ID:")
                                product = controller._getProductById(idd)
                                if product == None:
                                    print("\tTHIS PRODUCT DOESN'T EXISTS")
                                    break
                                nameCategory = ""
                                if product.getCategory() == False:
                                    nameCategory = "No category"
                                else:
                                    nameCategory = product.getCategory()[1]
                                ingredients = product.getIngredients()
                                messsage = ""
                                if len(ingredients) <= 0:
                                    message = "\tID - "+str(product.getId())+"\n\tName: "+str(product.getName())+"\n\tDescription: "+str(product.getDescription())+"\n\tPrice €: "+str(product.getPrice())+"\n\tCategory: "+str(nameCategory)+"\n\tNo ingredients"
                                    print(message)
                                    print()
                                else:
                                    message = "\tID - "+str(product.getId())+"\n\tName: "+str(product.getName())+"\n\tDescription: "+str(product.getDescription())+"\n\tPrice €: "+str(product.getPrice())+"\n\tCategory: "+str(nameCategory)+"\n\tIngredients:\n\t\t"
                                    for i in ingredients:
                                        message += controller._getIngredientById(i).getName()+" | "
                                    print(message)
                                    print()

                            elif opRead == 2:
                                printAllProducts()

                            elif opRead == 0:
                                break

                    elif opP == 'U':
                        printAllProducts()
                        idd = input("Enter the product to update (his ID):")
                        product = controller._getProductById(idd)
                        if product == None:
                            print("\tThis product doesn't exists")
                        else:
                            updatedCategory = False
                            while(True):
                                print("What param do you want to update?:")
                                print("1- Name ",product.getName())
                                print("2- Description ",product.getDescription())
                                print("3- Price ",product.getPrice())
                                if product.getCategory() == False:
                                    print("4- Category: Without category")
                                else:
                                    if updatedCategory:
                                        print("4- Category "+str(product.getCategory())+"-"+str(controller._getCategoryById(product.getCategory()).getName()))
                                    else:
                                        print("4- Category "+str(product.getCategory()[0])+"-"+str(product.getCategory()[1]))
                                print("5- Ingredients ",product.getIngredients())
                                print("6- Update")
                                print("0- Exit")
                                opParam = int(input("Choose a param: "))
                                if opParam == 1:
                                    name = input("Enter the new name: ")
                                    product.setName(name)
                                
                                elif opParam == 2:
                                    description = input("Enter the new description: ")
                                    product.setDescription(description)

                                elif opParam == 3:
                                    price = float(input("Enter the new price €: "))
                                    product.setPrice(price)

                                elif opParam == 4:
                                    print("We have the following categories:")
                                    allCategories = controller._getCategories()
                                    for id,cat in allCategories.items():
                                        print("\t",id,"-",cat.getName())
                                    newCatId = int(input("Enter a the new category id: "))
                                    product.setCategory(newCatId)
                                    updatedCategory = True

                                elif opParam == 5:
                                    print("We have the following ingredients:")
                                    allIngredients = controller._getIngredients()
                                    for id,ing in allIngredients.items():
                                        print("\t",id,"-",ing.getName())
                                    ingIds = []
                                    while(True):
                                        ingId = int(input("Enter the ID of the ingredients inside this products (0 to end):"))
                                        if ingId == 0:
                                            break
                                        else:
                                            ingIds.append(ingId)
                                    product.setIngredients(ingIds)

                                elif opParam == 6:
                                    if controller._updateProduct(product):
                                        print("\tProduct updated")
                                        break
                                    else:
                                        print("\tERROR. Not updated")

                                elif opParam == 0:
                                    break
                    
                    elif opP == 'D':
                        printAllProducts()
                        idd = input("Enter the product ID to remove:")
                        produuct = controller._getProductById(idd)
                        if produuct == None:
                            print("\tError. This product doesn't exists")
                        else:
                            if controller._deleteProduct(idd):
                                print("\tProduct removed")
                            else:
                                print("\tERROR. Not removed")
            

    
