class Ingredient():

    def __init__(self,id,name,typeI,observations,products):
        self.__id = id
        self.__name = name
        self.__typeI = typeI
        self.__observations = observations
        self.__products = products

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getName(self):
        return self.__name

    def getTypeI(self):
        return self.__typeI
    
    def getObservations(self):
        return self.__observations
    
    def getProducts(self):
        return self.__products

    def setProducts(self,products):
        self.__products = products