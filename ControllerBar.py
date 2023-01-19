from ApiBar import ApiBar
api = ApiBar()

class ControllerBar():

    def __init__(self):
        self.__categories = api.getCategories()
        self.__products = api.getProducts()
        self.__ingredients = api.getIngredients()
        self.__orders = api.getOrders()
        self.__lines = api.getLines()

    def getNumCategories(self):
        return len(self.__categories)

    def getNumProducts(self):
        return len(self.__products)

    def getNumIngredients(self):
        return len(self.__ingredients)

    def getNumOrders(self):
        return len(self.__orders)

    def getNumLines(self):
        return len(self.__lines)

    def getOrderTableById(self,id):
        order = self._getOrderById(id)
        return order.getTable()

    def getProductNameById(self,id):
        product = self._getProductById(id)
        return product.getName()

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
    def _getOrderById(self,id):
        return api.getOrderById(id)
    def _getLineById(self,id):
        return api.getLineById(id)

    #GET ALL
    #RETURN LIST OF OBJECTS LIST[idObject] = OBJECT
    def _getIngredients(self):
        return api.getIngredients()
    def _getProducts(self):
        return api.getProducts()
    def _getCategories(self):
        return api.getCategories()
    def _getOrders(self):
        return api.getOrders()
    def _getLines(self):
        return api.getLines()

    #ADD
    #RETURN TRUE OR FALSE
    #PARAM: OBJECT WIH ID NONE
    def _addIngredient(self,ing):
        return api.addIngredient(ing)
    def _addCategory(self,cat):
        return api.addCategory(cat)
    def _addProduct(self,prod):
        return api.addProduct(prod)
    def _addOrder(self,order):
        return api.addOrder(order)
    def _addLine(self,line):
        return api.addLine(line)

    #UPDATE
    #RETURN TRUE OR FALSE
    #PARAM: OBJECT WITH FULL INFORMATION
    def _updateIngredient(self,ing):
        return api.updateIngredient(ing)
    def _updateCategory(self,cat):
        return api.updateCategory(cat)
    def _updateProduct(self,prod):
        return api.updateProduct(prod)
    def _updateOrder(self,order):
        return api.updateOrder(order)
    def _updateLine(self,line):
        return api.updateLine(line)

    #DELETE
    #RETURN TRUE OR FALSE
    #PARAM: ID
    def _deleteIngredient(self,id):
        return api.deleteIngredient(id)
    def _deleteCategory(self,id):
        return api.deleteCategory(id)
    def _deleteProduct(self,id):
        return api.deleteProduct(id)
    def _deleteOrder(self,id):
        return api.deleteOrder(id)
    def _deleteLine(self,id):
        return api.deleteLine(id)


    def _confirmOrder(self,order):
        return api.confirmOrder(order)