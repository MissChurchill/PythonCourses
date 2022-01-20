menus = [['Egg Sandwich', 'Bagel', 'Coffee'],
        ['BLT', 'PB&J', 'Turkey Sandwich'],
        ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print(menus[0][1])


menus = { 'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
        'Lunch':['BLT', 'PB&J', 'Turkey Sandwich'],
        'Dinner':['Soup', 'Salad', 'Spaghetti', 'Taco']}

print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch Menu:\t', menus['Lunch'])
print('Dinner Menu:\t', menus['Dinner'])

#items method and loop
for name, menu in menus.items():
    print(name, ':', menu)
    
    