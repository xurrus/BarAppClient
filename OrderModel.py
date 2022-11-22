
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

    def addNewProduct(self,numProduct,product,quantity):
        self.__listProducts[numProduct] = [product,quantity]
        for product,quantity in self.__listProducts.values():
            self.__pax += product.getPrice()*quantity
        return True

    def getNumOfProducts(self):
        num = 0
        for x in self.__listProducts:
            num = x
        return x

    def getNumOfProductByName(self,nameProduct):
        for numProduct,lista in self.__listProducts.items():
            product = lista[0]
            if nameProduct == product.getName():
                return numProduct

    def removeProductByNum(self,numProduct):
        self.__listProducts.pop(numProduct)
        self.__pax = 0
        for product,quantity in self.__listProducts.values():
            self.__pax += product.getPrice()*quantity
        return True