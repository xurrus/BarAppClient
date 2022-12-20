
class Order():

    def __init__(self,table,client,waiter,listProducts):
        self.__table = table
        self.__active = True
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

    def getProducts(self):
        return self.__listProducts

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
        return None

    def removeProductByNum(self,numProduct):
        lista = self.getListByNumProduct(numProduct)
        if(lista[1] == 1):
            self.__listProducts.pop(numProduct)
        else:
            lista[1] -= 1
        self.__pax = 0
        for product,quantity in self.__listProducts.values():
            self.__pax += product.getPrice()*quantity
        return True

    def changeQuantityForAProductByName(self,nameProduct,quantity):
        changed = False
        for numProduct,lista in self.__listProducts.items():
            if nameProduct == lista[0].getName():
                lista[1] = quantity
                changed = True
                break
        self.__pax = 0
        for product,quantity in self.__listProducts.values():
            self.__pax += product.getPrice()*quantity
        return changed

    def getListByNumProduct(self,numProduct):
        lista =  self.__listProducts[numProduct]
        return lista

    def isActive(self):
        return self.__active

    def setActive(self,bool):
        self.__active = bool 