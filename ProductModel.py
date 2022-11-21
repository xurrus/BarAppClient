class Product():

    def __init__(self,id,name,description,price,category,ingredients):
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
    
    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getCategory(self):
        return self.__category

    def getIngredients(self):
        return self.__ingredients

    def setIngredients(self,ing):
        self.__ingredients = ing