#Difine the menu of cafe
menu = {
    'coffee': 60,
    'tea': 50,
    'sandwich': 100,
    'burger': 150,
    'pizza': 200,
    'salad': 80,
    'pasta': 120,
    'water bottle': 30,
    'coke': 40,
}
#Greet the user and display the menu
print("Welcome to Anthena Cafe!\n vilithe nalugu matalu kudhirithe cupu coffee!")
print("Here is the menu:")
print("Item\tPrice")
for item, price in menu.items():
    print(f"{item}\t{price} Rs")

order_total = 0
ordered_items = []

#Take orders from the user
i = 1
while True:
    print(f"\nOrder {i}:")
    item = input("\nEnter the item you want to order: ").lower().strip()
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"{item} added to your order.")
    else:
        print(f"Sorry, {item} is not available.")

    another_order = input("Do you want to order another item? (yes/no): ").lower().strip()
    i += 1
    if another_order != 'yes':
      
        break
        
#Bill generation
print('\n your ordered items are: ')
for items in ordered_items:
    print(f"- {items} ({menu[items]} Rs)")
print(f"\nYour total bill is: {order_total} Rs")
print("Thank you for visiting the Cafe!")
#End of the cafe program


                    