from pyscript import display

restaurant_name = "Café de Reyes" #string
owner_name = "David Miguel A. Reyes" #string
established_year = 1995 #integer
popular_item_price = 250 #float
has_delivery_service = True #boolean
product_names = ["Steak frites", "Croissant", "Pasta", "Fries", "Iced Tea"] #list
business_hours = "9:00 AM - 11:00 PM" #string
menu_price = { #dictionary
    "Steak frites": 90.00,
    "Croissant": 150.00,
    "Pasta": 120.00,
    "Fries": 85.00,
    "Iced Tea": 75.00,
}

#list of strings
common_allergns = ["Eggs", "Fish", "Milk"]
#float
tax_rate = 0.09

# info
display(restaurant_name, target="restaurant")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {established_year}", target="year")

# Display info
display(f"Open: {business_hours}", target="hours")
display(f'Delivery Available: {"From Mon-Sat" if has_delivery_service else "No"}', target="delivery")
display(f"Common Allergens: {', '.join(common_allergns)}", target="allergens")
display(f"Tax Rate: {tax_rate*100:.0f}%", target="tax")