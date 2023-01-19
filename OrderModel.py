
class Order():

    def __init__(self,id,table,client,state,waiter,price,lines):
        if id == None:
            self.__id = 0
        else:
            self.__id = id
        self.__table = table
        self.__client = client
        self.__state = state
        self.__waiter = waiter
        if price == None:
            self.__price = None
        else:
            self.__price = price
        if lines == None:
            self.__lines = None
        else:
            self.__lines = lines

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def getTable(self):
        return self.__table
    
    def setTable(self,t):
        self.__table = t

    def getClient(self):
        return self.__client

    def setClient(self,c):
        self.__client = c

    def getState(self):
        return self.__state

    def setState(self,st):
        self.__state = st

    def getWaiter(self):
        return self.__waiter

    def setWaiter(self,w):
        self.__waiter = w

    def getPrice(self):
        return self.__price

    def setPrice(self,p):
        self.__price = p

    def getLines(self):
        return self.__lines

    def setLines(self,l):
        self.__lines = l


    '''
    METHODS FOR OLD ORDER (LOCAL ORDER)
    '''
    # def addNewProduct(self,numProduct,product,quantity):
    #     self.__listProducts[numProduct] = [product,quantity]
    #     for product,quantity in self.__listProducts.values():
    #         self.__pax += product.getPrice()*quantity
    #     return True

    # def getNumOfProducts(self):
    #     num = 0
    #     for x in self.__listProducts:
    #         num = x
    #     return x

    # def getNumOfProductByName(self,nameProduct):
    #     for numProduct,lista in self.__listProducts.items():
    #         product = lista[0]
    #         if nameProduct == product.getName():
    #             return numProduct
    #     return None

    # def removeProductByNum(self,numProduct):
    #     lista = self.getListByNumProduct(numProduct)
    #     if(lista[1] == 1):
    #         self.__listProducts.pop(numProduct)
    #     else:
    #         lista[1] -= 1
    #     self.__pax = 0
    #     for product,quantity in self.__listProducts.values():
    #         self.__pax += product.getPrice()*quantity
    #     return True

    # def changeQuantityForAProductByName(self,nameProduct,quantity):
    #     changed = False
    #     for numProduct,lista in self.__listProducts.items():
    #         if nameProduct == lista[0].getName():
    #             lista[1] = quantity
    #             changed = True
    #             break
    #     self.__pax = 0
    #     for product,quantity in self.__listProducts.values():
    #         self.__pax += product.getPrice()*quantity
    #     return changed

    # def getListByNumProduct(self,numProduct):
    #     lista =  self.__listProducts[numProduct]
    #     return lista
