class Category():
    
    def __init__(self,id,name,products):
        self.__id = id
        self.__name = name
        self.__products = products

    def getName(self):
        return self.__name

    def setProducts(self,products):
        self.__products = products

    def getProducts(self):
        return self.__products

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def toString(self):
        return str(self.__id)+" "+str(self.__name)+" "+str(self.__products)