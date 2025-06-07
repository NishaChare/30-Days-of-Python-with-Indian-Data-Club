# inventory tracker using dictionaries

inventory = {'Apples': 10, 'Bananas': 5, 'Oranges': 8}

# Add items
inventory['Grapes'] = 12

# Update quantity
inventory['Apples'] += 5

# Remove item
del inventory['Bananas']

# Display inventory

for item, qty in inventory.items():
    print(f"{item}: {qty}")
