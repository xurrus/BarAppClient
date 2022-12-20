class Product():

    def __init__(self,id,name,description,price,category,ingredients):
        if(id == None):
            self.__id = 0
        else:
            self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__ingredients = ingredients

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self,n):
        self.__name = n
    
    def getDescription(self):
        return self.__description

    def setDescription(self,d):
        self.__description = d

    def getPrice(self):
        return self.__price

    def setPrice(self,p):
        self.__price = p

    def getCategory(self):
        return self.__category

    def setCategory(self,c):
        self.__category = c

    def getIngredients(self):
        return self.__ingredients

    def setIngredients(self,ing):
        self.__ingredients = ing

    def toString(self):
        message = str(self.__id)+": Name "+str(self.__name)+", Description:"+str(self.__description)+", Price:"+str(self.__price)+", Category: "+str(self.__category)+", Ingredients"
        for i in self.__ingredients:
            message += str(i)+" "
        return message