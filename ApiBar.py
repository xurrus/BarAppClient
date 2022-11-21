import requests
from CategoryModel import Category
from ProductModel import Product
from IngredientModel import Ingredient

class ApiBar():

    def getCategories(self):

        url = "http://localhost:8069/bar_app/categories"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            return None

        json = {}
        listCategories = {}

        json = data["data"]
        for x in json:
            idd = x["id"]
            name = x["name"]
            products = x["products"]
            newCategoria = Category(idd,name,products)
            #print(newCategoria.toString())
            listCategories[idd] = newCategoria
        
        return listCategories

    def getProducts(self):
        
        url = "http://localhost:8069/bar_app/products"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            return None

        json = {}
        listProducts = {}

        json = data["data"]
        for x in json:
            idd = x["id"]
            name = x["name"]
            description = x["description"]
            price = x["price"]
            category = x["category"]
            ingredients = x["ingredients"]
            newProducto = Product(idd,name,description,price,category,ingredients)
            listProducts[idd] = newProducto
        
        return listProducts

    def getIngredients(self):
        
        url = "http://localhost:8069/bar_app/ingredients"
        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
        else:
            return None

        json = {}
        listIngredients = {}

        json = data["data"]
        for x in json:
            idd = x["id"]
            name = x["name"]
            typeI = x["typeI"]
            observations = x["observations"]
            products = x["products"]
            ingredient = Ingredient(idd,name,typeI,observations,products)
            listIngredients[idd] = ingredient
        
        return listIngredients
