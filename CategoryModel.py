class Category():
    
    def __init__(self,id,name,fullName,products,parentId):
        if(id == None):
            self.__id = 0
        else:
            self.__id = id
        self.__id = id
        self.__name = name
        if fullName == None:
            self.__fullName = None
        else:
            self.__fullName = fullName
        self.__products = products
        if parentId == None:
            self.__parentId = False
        else:
            self.__parentId = parentId

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

    def getFullName(self):
        return self.__fullName
    
    def setFullName(self,f):
        self.__fullName = f

    def getParentId(self):
        return self.__parentId
    
    def setParentId(self,id):
        self.__parentId = id

    def toString(self):
        message = str(self.__id)+": Name "+str(self.__name)+", Products: "
        for p in self.__products:
            message += str(p)+" "
        return message