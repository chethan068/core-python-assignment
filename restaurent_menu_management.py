def add_item(menu, item):
    
    if item not in menu:
        menu.append(item)
        print(f"Added {item} to the menu.")
    else:
        print(f"{item} is already on the menu.")

def remove_item(menu, item):
    
    if item in menu:
        menu.remove(item)
        print(f"Removed {item} from the menu.")
    else:
        print(f"{item} is not on the menu.")

def check_item(menu, item):
    
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item(initial_menu, "Tacos")  
remove_item(initial_menu, "Salad")  
print(f"Updated menu: {initial_menu}")
check_item(initial_menu, "Pizza") 

