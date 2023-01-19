import requests
from CategoryModel import Category
from ProductModel import Product
from IngredientModel import Ingredient
from OrderModel import Order
from LineModel import Line

class ApiBar():
    #############################################################
    ####################### INGREDIENT ################################
    #############################################################

    ##GET ONE INGREDIENT BY ID
    #PARAM: ID OF THE INGREDIENT
    #RETURN ONE INGREDIENT OBJECT
    def getIngredientById(self,id):
        url = "http://localhost:8069/bar_app/getIngredient/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if len(json) == 0:
            return None
        for x in json:
            idd = x["id"]
            name = x["name"]
            typeI = x["typeI"]
            observations = x["observations"]
            products = x["products"]
            newIngredient = Ingredient(idd,name,typeI,observations,products)

        return newIngredient

    ##GET ALL INGREDIENTS
    #RETURN A LIST OF INGREDIENTS: LIST[INGREDIENT.ID] = INGREDIENT
    def getIngredients(self):
        url = "http://localhost:8069/bar_app/getIngredients"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listIngredients = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            name = x["name"]
            typeI = x["typeI"]
            observations = x["observations"]
            products = x["products"]
            newIngredient = Ingredient(idd,name,typeI,observations,products)
            listIngredients[idd] = newIngredient

        return listIngredients

    ##POST ONE INGREDIENT
    #PARAM: OBJECT INGREDIENT WITH NONE ID
    #RETURN BOOLEAN
    #AFTER INSERT OBJECT INTO DATABASE, UPDATES ITS ID WITH THE GENERATED
    def addIngredient(self,ing):
        url = "http://localhost:8069/bar_app/addIngredient"
        params = {
            "name":ing.getName(),
            "typeI":ing.getTypeI(),
            "observations":ing.getObservations(),
            "products":ing.getProducts()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            jsonId = jsonReturned['result']['id']
            ing.setId(jsonId)
            return True
        else:
            print("Error posting")
            return False

    ##UPDATE ONE INGREDIENT  
    #PARAM: OBJECT INGREDIENT WITH ALL INFORMATION
    #RETURN BOOLEAN
    def updateIngredient(self,ing):
        url = "http://localhost:8069/bar_app/updateIngredient"
        params = {
            "id":ing.getId(),
            "name":ing.getName(),
            "typeI":ing.getTypeI(),
            "observations":ing.getObservations(),
            "products":ing.getProducts()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    #DELETE ONE INGREDIENT
    #PARAM: EXISTING ID
    def deleteIngredient(self,id):
        url = "http://localhost:8069/bar_app/deleteIngredient"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False


    #############################################################
    ####################### CATEGORY ################################
    #############################################################

    ##GET ONE CATEGORY BY ID
    #PARAM: ID OF THE CATEGORY
    #RETURN ONE CATEGORY OBJECT
    def getCategoryById(self,id):
        url = "http://localhost:8069/bar_app/getCategory/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if (len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                name = x["name"]
                fullName = x["full_name"]
                products = x["products"]
                if x["parent_id"] == False:
                    parentId = x["parent_id"]
                else:
                    parentId = x["parent_id"][0]
                newCategory = Category(idd,name,fullName,products,parentId)

            return newCategory

    ##GET ALL CATEGORIES
    #RETURN A LIST OF CATEGORIES: LIST[CATEGORY.ID] = CATEGORY
    def getCategories(self):
        url = "http://localhost:8069/bar_app/getCategories"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listCategories = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            name = x["name"]
            fullName = x["full_name"]
            products = x["products"]
            if x["parent_id"] == False:
                parentId = x["parent_id"]
            else:
                parentId = x["parent_id"][0]
            newCategory = Category(idd,name,fullName,products,parentId)
            listCategories[idd] = newCategory

        return listCategories

    ##POST ONE CATEGORY
    #PARAM: OBJECT CATEGORY WITH ID NONE
    #RETURN BOOLEAN
    def addCategory(self,cat):
        url = "http://localhost:8069/bar_app/addCategory"
        params = {
            "name":cat.getName(),
            "products":cat.getProducts(),
            "parent_id":cat.getParentId()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            jsonId = jsonReturned['result']['id']
            fullName = jsonReturned['result']['full_name']
            cat.setId(jsonId)
            cat.setFullName(fullName)
            return True
        else:
            print("Error posting")
            return False

    ##UPDATE ONE CATEGORY
    #PARAM: CATEGORY OBJECT WITH ALL INFORMATION
    #RETURN BOOLEAN
    def updateCategory(self,cat):
        url = "http://localhost:8069/bar_app/updateCategory"
        params = {
            "id":cat.getId(),
            "name":cat.getName(),
            "products":cat.getProducts(),
            "parent_id":cat.getParentId()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            fullName = jsonReturned['result']['full_name']
            cat.setFullName(fullName)
            return True
        else:
            return False

    ##DELETE ONE CATEGORY
    #PARAM: EXISTING ID
    #RETURN BOOLEAN
    def deleteCategory(self,id):
        url = "http://localhost:8069/bar_app/deleteCategory"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    #############################################################
    ####################### PRODUCT ################################
    #############################################################

    ##GET ONE PRODUCT BY ID
    #PARAM : ID
    #RETURN ONE PRODUCT OBJECT
    def getProductById(self,id):
        url = "http://localhost:8069/bar_app/getProduct/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if(len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                name = x["name"]
                price = x["price"]
                description = x["description"]
                category = x["category"]
                ingredients = x["ingredients"]
                newProduct = Product(idd,name,description,price,category,ingredients)

        return newProduct

    ##GET ALL PRODUCTS
    #RETURN A LIST OF PRODUCTS: LIST[PRODUCT.ID] = PRODUCT
    def getProducts(self):
        url = "http://localhost:8069/bar_app/getProducts"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listProducts = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            name = x["name"]
            price = x["price"]
            description = x["description"]
            category = x["category"]
            ingredients = x["ingredients"]
            newProduct = Product(idd,name,description,price,category,ingredients)
            listProducts[idd] = newProduct

        return listProducts

    ##POST ONE PRODUCT    
    #PARAM: OBJECT PRODUCT WITH NONE ID
    # RETURN BOOLEAN
    def addProduct(self,prod):
        url = "http://localhost:8069/bar_app/addProduct"
        params = {
            "name":prod.getName(),
            "description":prod.getDescription(),
            "price":prod.getPrice(),
            "category":prod.getCategory(),
            "ingredients":prod.getIngredients()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            jsonId = jsonReturned['result']['id']
            prod.setId(jsonId)
            return True
        else:
            print("Error posting")
            return False

    ##UPDATE ONE PRODUCT  
    #PARAM: OBJECT PRODUCT WITH ALL INFORMATION
    #RETURN BOOLEAN
    def updateProduct(self,prod):
        url = "http://localhost:8069/bar_app/updateProduct"
        params = {
            "id":prod.getId(),
            "name":prod.getName(),
            "price":prod.getPrice(),
            "description":prod.getDescription(),
            "category":prod.getCategory(),
            "ingredients":prod.getIngredients()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    ##DELETE ONE PRODUCT
    #PARAM: EXISTING ID
    #RETURN BOOLEAN
    def deleteProduct(self,id):
        url = "http://localhost:8069/bar_app/deleteProduct"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    #############################################################
    ####################### ORDER ################################
    #############################################################

    ##GET ONE ORDER BY ID
    #PARAM : ID
    #RETURN ONE ORDER OBJECT
    def getOrderById(self,id):
        url = "http://localhost:8069/bar_app/getOrder/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if(len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                table = x["table"]
                client = x["client"]
                state = x["state"]
                waiter = x["waiter"]
                price = x["price"]
                lines = x["lines"]
                newOrder = Order(idd,table,client,state,waiter,price,lines)

        return newOrder

    ##GET ALL ORDERS
    #RETURN A LIST OF ORDERS: LIST[ORDER.ID] = ORDER
    def getOrders(self):
        url = "http://localhost:8069/bar_app/getOrders"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listOrders = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            table = x["table"]
            client = x["client"]
            state = x["state"]
            waiter = x["waiter"]
            price = x["price"]
            lines = x["lines"]
            newOrder = Order(idd,table,client,state,waiter,price,lines)
            listOrders[idd] = newOrder

        return listOrders

    ##POST ONE ORDER    
    #PARAM: OBJECT ORDER WITH NONE ID
    # RETURN BOOLEAN
    def addOrder(self,order):
        url = "http://localhost:8069/bar_app/addOrder"
        params = {
            "table":order.getTable(),
            "client":order.getClient(),
            "state":order.getState(),
            "waiter":order.getWaiter(),
            "price":order.getPrice(),
            "lines":order.getLines()
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']['id']
                order.setId(jsonId)
                return True
            else:
                print("Error posting")
                return False
        else:
            print("Error posting")
            return False

    ##UPDATE ONE ORDER  
    #PARAM: OBJECT ORDER WITH ALL INFORMATION
    #RETURN BOOLEAN
    def updateOrder(self,order):
        url = "http://localhost:8069/bar_app/updateOrder"
        params = {
            "id":order.getId(),
            "table":order.getTable(),
            "client":order.getClient(),
            "state":order.getState(),
            "waiter":order.getWaiter(),
            "price":order.getPrice(),
            "lines":order.getLines()
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    ##DELETE ONE ORDER
    #PARAM: EXISTING ID
    #RETURN BOOLEAN
    def deleteOrder(self,id):
        url = "http://localhost:8069/bar_app/deleteOrder"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False


    #############################################################
    ####################### LINE ORDER ##########################
    #############################################################

    ##GET ONE LINE BY ID
    #PARAM : ID
    #RETURN ONE LINE OBJECT
    def getLineById(self,id):
        url = "http://localhost:8069/bar_app/getLine/"+str(id)
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        json = data["data"]
        if(len(json) == 0):
            return None
        else:
            for x in json:
                idd = x["id"]
                orderId = x["order_id"][0]
                productId = x["product_id"][0]
                quantity = x["quantity"]
                fullName = x["fullName"]
                newLine = Line(idd,orderId,productId,quantity,fullName)

        return newLine

    ##GET ALL LINES
    #RETURN A LIST OF LINES: LIST[LINE.ID] = LINE
    def getLines(self):
        url = "http://localhost:8069/bar_app/getLines"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("Error GET")
            return None

        json = {}
        listLines = {}
        json = data["data"]
        
        for x in json:
            idd = x["id"]
            orderId = x["order_id"][0]
            productId = x["product_id"][0]
            quantity = x["quantity"]
            fullName = x["fullName"]
            newLine = Line(idd,orderId,productId,quantity,fullName)
            listLines[idd] = newLine

        return listLines

    ##POST ONE LINE    
    #PARAM: OBJECT LINE WITH NONE ID AND NO FULL NAME
    # RETURN BOOLEAN
    def addLine(self,line):
        url = "http://localhost:8069/bar_app/addLine"
        params = {
            "order_id":line.getOrderId(),
            "product_id":line.getProductId(),
            "quantity":line.getQuantity(),
        }
        r = requests.post(url=url,json=params)
        if (r.status_code == 200):
            jsonReturned = r.json()
            if (len(jsonReturned) > 0):
                jsonId = jsonReturned['result']['id']
                newFullName = jsonReturned['result']['full_name']
                line.setId(jsonId)
                line.setFullName(newFullName)
                return True
            else:
                print("Error posting")
                return False
        else:
            print("Error posting")
            return False

    ##UPDATE ONE LINE  
    #PARAM: OBJECT LINE WITH ALL INFORMATION, WITHOUT FULL NAME
    #RETURN BOOLEAN
    def updateLine(self,line):
        url = "http://localhost:8069/bar_app/updateLine"
        params = {
            "id":line.getId(),
            "order_id":line.getOrderId(),
            "product_id":line.getProductId(),
            "quantity":line.getQuantity(),
        }
        r = requests.put(url=url,json=params)
        if (r.status_code == 200):
            jsonreturned = r.json()
            newFullName = jsonreturned['result']['full_name']
            line.setFullName(newFullName)
            return True
        else:
            return False

    ##DELETE ONE LINE
    #PARAM: EXISTING ID
    #RETURN BOOLEAN
    def deleteLine(self,id):
        url = "http://localhost:8069/bar_app/deleteLine"
        params = {
            "id":id
        }
        r = requests.delete(url=url,json=params)
        if (r.status_code == 200):
            return True
        else:
            return False

    #############################################################
    ########## CONFIRM ORDER AND GENERATE INVOICE ###############
    #############################################################

    def confirmOrder(self,order):
        url = "http://localhost:8069/bar_app/confirmOrder/"+str(order.getId())
        response = requests.request("GET",url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("ERROR CONFIRMING")
            return None

        state = data['stateOrder']
        order.setState(state)
        return True