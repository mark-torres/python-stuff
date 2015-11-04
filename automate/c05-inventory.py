#! python3
# ==========
# = PART 1 =
# ==========

# display inventory
def displayInventory(inventory):
	totalItems = 0
	print('Inventory:')
	for key,value in inventory.items():
		print("  ",value, key)
		if str(value).isdecimal():
			totalItems += value
	print('Total number of items:', totalItems)

# ==========
# = PART 2 =
# ==========

# add to inventory
def addToInventory(inventory, addedItems):
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	return inventory

# part 1
inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inventory1)

# part 2
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory2 = {'gold coin': 42, 'rope': 1}

inventory2 = addToInventory(inventory2, dragonLoot)
displayInventory(inventory2)