class Product:
    def __init__(self, name, id, quantity):
        self.name = name
        self.id = id
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, name, id, quantity):
        product = Product(name, id, quantity)
        self.products.append(product)

    def buy_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                if product.quantity > 0:
                    product.quantity -= 1
                    print(f"Congratulations! You have successfully bought {product.name}.")
                else:
                    print(f"Sorry, {product.name} is out of stock.")
        print("Product not found.")

# Create a shop object
my_shop = Shop()

# Add some products to the shop
my_shop.add_product('Banana', 1, 25)
my_shop.add_product('Apple', 2, 10)
my_shop.add_product('Orange', 3, 0)  # Out of stock

# Try to buy a product
my_shop.buy_product(1)  # Should print "Congratulations! You have successfully bought Banana."
my_shop.buy_product(3) # Should print "Sorry, Orange is out of stock."
my_shop.buy_product(4)  # Should print "Product not found."
