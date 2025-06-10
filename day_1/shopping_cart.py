class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        return self.price * self.quantity

class shoppingCart:
    def __init__(self):
        self.cart=[]

    def add_product(self,product):
        for item in self.cart:
            if item.name == product.name:
                item.quantity += product.quantity 
                print(f"✅ Updated quantity of '{product.name}' in cart.")
                return
        self.cart.append(product)
        print(f"✅ Added '{product.name}' to cart.")

    def remove_product(self,product_name):
        for item in self.cart:
            if item.name == product_name:
                self.cart.remove(item)
                print(f"❌ Removed '{product_name}' from cart.")
                return
        print(f"❌ '{product_name}' not found in cart.")
    
    def show_cart(self):
        if not self.cart:
            print("🛒 Cart is empty.")
            return
        print("\n🛒 Cart contents : ")
        for product in self.cart:
            print(f"- {product.name} x {product.quantity} @ ${product.price:.2f} each = ${product.get_total_price():.2f}")
        print(f"Total Price: ${self.calculate_total_price():.2f}")

    def calculate_total_price(self):
        return sum(product.get_total_price() for product in self.cart)
    
if __name__ == "__main__":
    # Create cart
    cart = shoppingCart()

    # Add products
    cart.add_product(Product("Laptop", 1000, 1))
    cart.add_product(Product("Mouse", 25, 2))
    cart.add_product(Product("Laptop", 1000, 1))  # Test quantity update

    # Show contents
    cart.show_cart()

    # Remove a product
    cart.remove_product("Mouse")

    # Show updated cart
    cart.show_cart()
