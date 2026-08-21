
raw_delivery = [
    ("Apple", 0.75, 50),
    ("Banana", 0.40, 100),
    ("Milk", 2.50, 15),
    ("Bread", 1.80, 20),
    ("Apple", 0.75, 30)
]

shopping_cart = ["Apple","Apple","Milk","Dragonfruit","Bread"]

def build_inventory(delivery_data):
    inventory = {}
    for product_name, price, quantity in delivery_data:
       if product_name in inventory:
           inventory[product_name]["stock"] += quantity
       else:
           inventory[product_name] = {
               "price": float(price),
               "stock": int(quantity)
           }
    return inventory

def process_checkout(cart, inventory):
    receipt = []
    total_price = 0.0
    
    print("CheckOut Logs")
    for item in cart:
        if item in inventory:
            if inventory[item]["stock"] > 0:
               inventory[item]["stock"] -= 1
               price = inventory[item]["price"]
               
               receipt.append((item,price))
               total_price += price 
               
            else :
                print(f"{item} is Sold Out:")
        
        else:
            print(f"{item} is not carrid in stock")
            
    print("\n Final Receipt")
    for product, price in receipt:
           print(f"{product}: ${price:.2f}")
    
    print(f"Total_Price: ${total_price:.2f}")
    return receipt

store_inventory = build_inventory(raw_delivery)
customer_recepit = process_checkout(shopping_cart, store_inventory)
    

