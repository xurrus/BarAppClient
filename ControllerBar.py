from ApiBar import ApiBar
api = ApiBar()

class ControllerBar():

    def __init__(self):
        self.__categories = api.getCategories()
        self.__products = api.getProducts()
        self.__ingredients = api.getIngredients()
        self.__orders = {}

    def getCategories(self):
        return self.__categories

    def getProducts(self):
        return self.__products

    def getIngredients(self):
        return self.__ingredients

    def getCategoryById(self,id):
        return self.__categories[id]

    def getProductById(self,id):
        return self.__products[id]

    def getIngredientById(self,id):
        return self.__ingredients[id]

    def getNumCategories(self):
        return len(self.__categories)

    def getNumProducts(self):
        return len(self.__products)

    def getNumIngredients(self):
        return len(self.__ingredients)
        
    def getProductByName(self,name):
        for idd,prod in self.__products.items():
            if prod.getName() == name:
                return prod
        return None

    def addOrder(self,numOrder,order):
        self.__orders[numOrder] = order

    def getOrders(self):
        return self.__orders

    def getOrderByNum(self,numOrder):
        return self.__orders[numOrder]

    def changeOrder(self,numOrder,newOrder):
        self.__orders[numOrder] = newOrder
        return True
    
    def existsOrder(self,numOrder):
        if numOrder in self.__orders:
            return True
        return False

    #####################################################
    #################### API METHODS #####################
    #####################################################

    #GET ONE BY ID 
    #RETURN ONE OBJECT
    #PARAM: ID
    def _getIngredientById(self,id):
        return api.getIngredientById(id)
    def _getCategoryById(self,id):
        return api.getCategoryById(id)
    def _getProductById(self,id):
        return api.getProductById(id)

    #GET ALL
    #RETURN LIST OF OBJECTS LIST[idObject] = OBJECT
    def _getIngredients(self):
        return api.getIngredients()
    def _getProducts(self):
        return api.getProducts()
    def _getCategories(self):
        return api.getCategories()

    #ADD
    #RETURN TRUE OR FALSE
    #PARAM: OBJECT WIH ID NONE
    def _addIngredient(self,ing):
        return api.addIngredient(ing)
    def _addCategory(self,cat):
        return api.addCategory(cat)
    def _addProduct(self,prod):
        return api.addProduct(prod)

    #UPDATE
    #RETURN TRUE OR FALSE
    #PARAM: OBJECT WITH FULL INFORMATION
    def _updateIngredient(self,ing):
        return api.updateIngredient(ing)
    def _updateCategory(self,cat):
        return api.updateCategory(cat)
    def _updateProduct(self,prod):
        return api.updateProduct(prod)

    #DELETE
    #RETURN TRUE OR FALSE
    #PARAM: ID
    def _deleteIngredient(self,id):
        return api.deleteIngredient(id)
    def _deleteCategory(self,id):
        return api.deleteCategory(id)
    def _deleteProduct(self,id):
        return api.deleteProduct(id)