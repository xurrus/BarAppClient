from ControllerBar import ControllerBar

from LineModel import Line
from OrderModel import Order
from IngredientModel import Ingredient
from CategoryModel import Category
from ProductModel import Product

controller = ControllerBar()

def printAllIngredients():
    print()
    allIngredients = controller._getIngredients()
    print("Ingredients:")
    for id,ing in allIngredients.items():
        print("\tID ",id," - Name: ",ing.getName(),", Type: ",str(ing.getTypeI()))

def printAllCategories():
    print()
    allCategories = controller._getCategories()
    print("Categories:")
    for id,cat in allCategories.items():
        print("\tID ",id," - Full name: ",cat.getFullName())

def printAllProducts():
    print()
    allProducts = controller._getProducts()
    print("Products:")
    for id,pro in allProducts.items():
        if pro.getCategory() == False:
            nameCat = "no category"
        else:
            nameCat = pro.getCategory()[1]
        print("\tID ",id," - Name: ",pro.getName(),", Category: ",nameCat,", Price: ",pro.getPrice(),"€")

def printAllOrders():
    print()
    allOrders =  controller._getOrders()
    print("Orders:")
    for id,order in allOrders.items():
        print("\tID ",id," - Table: ",order.getTable(),", Price: ",order.getPrice(),"€, State: ",order.getState())

def printAllLines():
    print()
    allLines =  controller._getLines()
    print("Lines:")
    for id,line in allLines.items():
        print("\tID ",id," - Name: ",line.getFullName(),", Quantity: ",line.getQuantity())


while(True):
    print()
    print("## ORDERS MANAGEMENT ##")
    print(" 1. CRUD MENU")
    print(" 0. Exit")
    option = int(input("Select an option: "))
    #EXIT
    if (option == 0):
        print("BYE!")
        break

    #CRUD MENU
    elif option == 1:
        while(True):
            print()
            print("1- INGREDIENTS Management")
            print("2- CATEGORIES Management")
            print("3- PRODUCTS Management")
            print("4- ORDERS & LINES Management")
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
                        printAllProducts()
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
                                        message += str(controller._getProductById(p).getName())+"\n\t\t"
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
                                print("1- Name: ",ingredient.getName())
                                print("2- TypeI: ",ingredient.getTypeI())
                                print("3- Observations: ",ingredient.getObservations())
                                print("4- Products: ",ingredient.getProducts())
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
                                    printAllProducts()
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
                        printAllProducts()
                        prodIds = []
                        while(True):
                            prodId = int(input("Enter the ID of the product belonging to this category (0 to end):"))
                            if prodId == 0:
                                break
                            else:
                                prodIds.append(prodId)
                        printAllCategories()
                        parentId = int(input("If this new category is a child of another, enter its parent's ID (0 if not): "))
                        if parentId == 0:
                            parentId = False
                        newCategory = Category(None,name,None,prodIds,parentId)
                        if controller._addCategory(newCategory):
                            print("\tNew category ",newCategory.getFullName() ," added with id ",newCategory.getId())
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
                                father = category.getParentId()
                                #SI TIENE PRODUCTOS
                                if len(productos) > 0:
                                    if father == False:
                                        message = "\tID - "+str(category.getId())+"\n\tFull name: "+str(category.getFullName())+"\n\tCategory father: No one"+"\n\tProducts:\n\t\t"
                                    else:
                                        message = "\tID - "+str(category.getId())+"\n\tFull name: "+str(category.getFullName())+"\n\tCategory father: "+controller._getCategoryById(category.getParentId()).getFullName()+"\n\tProducts:\n\t\t"
                                    for p in productos:
                                        message += str(controller._getProductById(p).getName())+"\n\t\t"
                                    print(message)
                                    print()
                                #SI NO TIENE PRODUCTOS
                                else:
                                    if father == False:
                                        message = "\tID - "+str(category.getId())+"\n\tFull name: "+str(category.getFullName())+"\n\tCategory father: No one"+"\n\tNo products"
                                    else:
                                        message = "\tID - "+str(category.getId())+"\n\tFull name: "+str(category.getFullName())+"\n\tCategory father: "+controller._getCategoryById(category.getParentId()).getFullName()+"\n\tNo products"
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
                                print("1- Name: ",category.getName())
                                print("2- Products: ",category.getProducts())
                                if category.getParentId() == False:
                                    print("3- Category father: No one")
                                else:
                                    print("3- Category father: ",controller._getCategoryById(category.getParentId()).getFullName())
                                print("4- Update")
                                print("0- Exit")
                                opParam = int(input("Choose a param: "))
                                if opParam == 1:
                                    name = input("Enter the new name: ")
                                    category.setName(name)
                                
                                elif opParam == 2:
                                    printAllProducts()
                                    prodIds = []
                                    while(True):
                                        prodId = int(input("Enter the ID of the product inside this category (0 to end):"))
                                        if prodId == 0:
                                            break
                                        else:
                                            prodIds.append(prodId)
                                    category.setProducts(prodIds)


                                elif opParam == 3:
                                    printAllCategories()
                                    parentId = int(input("If this new category is a child of another, enter its parent's ID (0 if not): "))
                                    if parentId == 0:
                                        parentId = False
                                    category.setParentId(parentId)

                                elif opParam == 4:
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
                        printAllCategories()
                        catId = int(input("Enter the ID of the category for this product: "))
                        printAllIngredients()
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

            #ORDER CRUD
            elif opCRUD == 4:
                while(True):
                    print()
                    print("C) Create a new order")
                    print("R) Read")
                    print("U) Update a order")
                    print("D) Delete")
                    print("I) Confirm an order and invoice it")
                    print("0) Exit")
                    opO = input("Select an option: ")

                    if opO == '0':
                        break
                    
                    elif opO == 'C':
                        table = input("Table for the new order: ")
                        client = input("Client: ")
                        waiter = input("Waiter: ")
                        newOrder = Order(None,table,client,'A',waiter,None,None)
                        if controller._addOrder(newOrder):
                            print("\tNew order added with id ",newOrder.getId())
                        else:
                            print("\tError. Not added")
                        print("1) Add lines to this order")
                        print("0) Exit and continue")
                        opOC = int(input("What do you want to do now?: "))
                        if opOC == 1:
                            while True:
                                print("1) Create new line")
                                print("0) Exit and continue")
                                opOCC = int(input("Select an option: "))
                                if opOCC == 0:
                                    break
                                else:
                                    #MIENTRAS EL USUARIO QUIERA, VAMOS CREANDO LINEAS PARA ESTA ORDEN
                                    print("\nWe have the following products:")
                                    printAllProducts()
                                    productId = int(input("Enter the product to add to this line: "))
                                    quantity = int(input("Enter the quantity for this product: "))
                                    newLine = Line(None,newOrder.getId(),productId,quantity,None)
                                    if controller._addLine(newLine):
                                        print("New line added with ID ",newLine.getId()," and name",newLine.getFullName())
                                    else:
                                        print("Error. Not added")

                    elif opO == 'R':
                        while(True):
                            print("1- Read one order by ID")
                            print("2- Read all orders")
                            print("-----------------------")
                            print("3- Read one line by ID")
                            print("4- Read all lines")
                            print("0- Exit")
                            opRead = int(input("Choose an option:"))
                            if opRead == 1:
                                idd = input("Enter the order ID:")
                                order = controller._getOrderById(idd)
                                if order == None:
                                    print("\tTHIS ORDER DOESN'T EXISTS")
                                    break
                                lines = order.getLines()
                                messsage = ""
                                if len(lines) <= 0:
                                    message = "\tID - "+str(order.getId())+"\n\tTable: "+str(order.getTable())+"\n\tClient: "+str(order.getClient())+"\n\State: "+str(order.getState())+"\n\tWaiter: "+str(order.getWaiter())+"\n\tPrice €: "+str(order.getPrice())+"\n\tNo lines"
                                    print(message)
                                    print()
                                else:
                                    message = "\tID - "+str(order.getId())+"\n\tTable: "+str(order.getTable())+"\n\tClient: "+str(order.getClient())+"\n\State: "+str(order.getState())+"\n\tWaiter: "+str(order.getWaiter())+"\n\tPrice €: "+str(order.getPrice())+"\n\tLines:\n\t\t"
                                    for l in lines:
                                        message += controller._getLineById(l).getFullName()+" | "
                                    print(message)
                                    print()

                            elif opRead == 2:
                                printAllOrders()

                            elif opRead == 3:
                                idd = input("Enter the line ID:")
                                line = controller._getLineById(idd)
                                if line == None:
                                    print("\tTHIS LINE DOESN'T EXISTS")
                                    break
                                message = "\tID - "+str(line.getId())+"\n\tOrder: "+str(controller.getOrderTableById(line.getOrderId()))+"\n\tClient: "+str(controller.getProductNameById(line.getProductId()))+"\n\tQuantity: "+str(line.getQuantity())+"\n\tFull name: "+str(line.getFullName())
                                print(message)
                                print()

                            elif opRead == 4:
                                printAllLines()

                            elif opRead == 0:
                                break

                    elif opO == 'U':
                        printAllOrders()
                        idd = input("Enter the order to update (his ID):")
                        order = controller._getOrderById(idd)
                        if order == None:
                            print("\tThis order doesn't exists")
                        else:
                            while(True):
                                print("What param do you want to update?:")
                                print("1- Table ",order.getTable())
                                print("2- Client ",order.getClient())
                                print("3- Waiter ",order.getWaiter())
                                print("4- Lines ",order.getLines())
                                print("5- Update")
                                print("0- Exit")
                                opParam = int(input("Choose a param: "))
                                if opParam == 1:
                                    table = input("Enter the new table name: ")
                                    order.setTable(table)
                                
                                elif opParam == 2:
                                    client = input("Enter the new client: ")
                                    order.setClient(client)

                                elif opParam == 3:
                                    waiter = input("Enter the new waiter: ")
                                    order.setWaiter(waiter)

                                elif opParam == 4:
                                    print("We have the following lines:")
                                    lines = controller._getOrderById(idd).getLines()
                                    for lin in lines:
                                        print("\t",lin.getFullName())
                                    idd = int(input("Select a line to update: "))
                                    lineU = controller._getLineById(idd)
                                    while True:
                                        print("What do u want to update?")
                                        print("1) Product")
                                        print("2) Quantity")
                                        print("0) Exit")
                                        opOU = int(input("Select an option: "))
                                        if opOU == 1:
                                            printAllProducts()
                                            idd = int(input("Enter the new product for this line: "))
                                            lineU.setProductId(idd)
                                        elif opOU == 2:
                                            quantity = int(input("Enter a new quantity for the product: "))
                                            lineU.setQuantity(quantity)
                                        elif opOU == 0:
                                            break

                                elif opParam == 5:
                                    if controller._updateOrder(order):
                                        print("\Order updated")
                                        break
                                    else:
                                        print("\tERROR. Not updated")

                                elif opParam == 0:
                                    break
                    
                    elif opO == 'D':
                        while True:
                            print("1) Delete an order")
                            print("2) Delete a line")
                            print("0) Exit")
                            opOD = int(input("Select an option: "))
                            if opOD == 0:
                                break
                            elif opOD == 1:
                                printAllOrders()
                                idd = input("Enter the order ID to remove:")
                                orderD = controller._getOrderById(idd)
                                if orderD == None:
                                    print("\tError. This order doesn't exists")
                                else:
                                    if controller._deleteOrder(idd):
                                        print("\tOrder removed")
                                    else:
                                        print("\tERROR. Not removed")

                            elif opOD == 2:
                                printAllLines()
                                idd = input("Enter the line ID to remove:")
                                lineD = controller._getLineById(idd)
                                if lineD == None:
                                    print("\tError. This line doesn't exists")
                                else:
                                    if controller._deleteLine(idd):
                                        print("\tLine removed")
                                    else:
                                        print("\tERROR. Not removed")

                    elif opO == 'I':
                        printAllOrders()
                        idd = input("Enter the order to update (his ID):")
                        order = controller._getOrderById(idd)
                        if order == None:
                            print("\tThis order doesn't exists")
                        else:
                            if order.getState() == 'A':
                                print("Order state: ",order.getState())
                                confirm = int(input("CONFIRM ORDER? (1-YES | 0-NO)"))
                                if confirm == 1:
                                    if controller._confirmOrder(order):
                                        print("Order confirmed (state:",order.getState(),")")
                                    else:
                                        print("Error. Not confirmed")
                                elif confirm == 0:
                                    break

                            else:
                                print("You can't finish this order, is already confirmed")