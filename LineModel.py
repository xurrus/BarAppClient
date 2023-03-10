class Line():

    def __init__(self,idd,orderId,productId,quantity,fullName,observations) -> None:
        if idd == None:
            self.__id = 0
        else:
            self.__id = idd
        self.__orderId = orderId
        self.__productId = productId
        self.__quantity = quantity
        if fullName == None:
            self.__fullName = "No full name"
        else:
            self.__fullName = fullName
        if observations==None or observations==False or observations=="":
            self.__observations = "No observations"
        else:
            self.__observations = observations


    def getId(self):
        return self.__id

    def setId(self,idd):
        self.__id = idd

    def getOrderId(self):
        return self.__orderId

    def setOrderId(self,orderId):
        self.__orderId = orderId

    def getProductId(self):
        return self.__productId

    def setProductId(self,prodId):
        self.__productId = prodId

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self,q):
        self.__quantity = q

    def getFullName(self):
        return self.__fullName

    def setFullName(self,name):
        self.__fullName = name

    def getObservations(self):
        return self.__observations

    def setObservations(self,o):
        self.__observations = o