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