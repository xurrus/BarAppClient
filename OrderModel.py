
class Order():

    def __init__(self,table,client,waiter,listProducts):
        self.__table = table
        self.__client = client
        self.__pax = 0
        self.__waiter = waiter
        self.__listProducts = listProducts
        for product,quantity in self.__listProducts.values():
            self.__pax += product.getPrice()*quantity
    def getTable(self):
        return self.__table

    def getClient(self):
        return self.__client

    def getWaiter(self):
        return self.__waiter

    def printProducts(self):
        for product,quantity in self.__listProducts.values():
            print("\t\tName: ",product.getName(),", quantity: ",quantity)

    def getPax(self):
        return self.__pax