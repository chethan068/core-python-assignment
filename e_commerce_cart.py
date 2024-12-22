def calculate(cart):
    
    if not cart:
        return "The cart is empty."
    
    
    total_price = sum(cart.values())
    
   
    if len(cart) > 5:
        total_price *= 0.9  
    
    return f"Total Price: {total_price}"

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate(cart_items))
