class Ingredient():

    def __init__(self,id,name,typeI,observations,products):
        if(id == None):
            self.__id = 0
        else:
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

    def setName(self,n):
        self.__name = n

    def getTypeI(self):
        return self.__typeI
    
    def setTypeI(self,t):
        self.__typeI = t

    def getObservations(self):
        return self.__observations

    def setObservatons(self,obv):
        self.__observations = obv
        
    def getProducts(self):
        return self.__products

    def setProducts(self,products):
        self.__products = products

    def toString(self):
        message = str(self.__id)+": Name "+str(self.__name)+", Observations: "+str(self.__observations)+", Products: "
        for p in self.__products:
            message += str(p)+" "
        return message