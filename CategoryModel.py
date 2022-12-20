class Category():
    
    def __init__(self,id,name,products):
        if(id == None):
            self.__id = 0
        else:
            self.__id = id
        self.__id = id
        self.__name = name
        self.__products = products

    def getName(self):
        return self.__name

    def setName(self,n):
        self.__name = n

    def setProducts(self,products):
        self.__products = products

    def getProducts(self):
        return self.__products

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def toString(self):
        message = str(self.__id)+": Name "+str(self.__name)+", Products: "
        for p in self.__products:
            message += str(p)+" "
        return message