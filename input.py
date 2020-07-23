import add_item_to_db

new_input = []

print('input your item data here')
new_input.append(input('Input item category: ').upper())
new_input.append(input('Input item brand: ').upper())

add_item_to_db.main(new_input)

print('Your items were added to the database')