grocery_item = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_item.append(item)
def remove_item(item):
     grocery_item.remove(item)
display = lambda item:print("item:",item)
def count_characters(items):
    if not items:
            return 0
    return len(items[0])+count_characters(items[1:])
add_item("butter")
remove_item("bread")
for item in grocery_item:
    display(item)
print("Total characters in grocery items:",count_characters(grocery_item))

# You are helping a shopper manage their grocery shopping list. Your task is to create a simple Python program that does the following steps in order:

# Initial Grocery List:
# Create a list with the initial items: ["milk", "bread", "eggs"].
# Add Item Function:
#   Write a function add_item(item) that adds a given item (string) to the grocery list.
# Remove Last Item Function:
#   Write a function remove_last_item() that removes the last item from the grocery list.
# Lambda Function for Display:
# Use a lambda function to print each item in the list with the format: "Item: <item>".
# Recursive Character Count (Bonus):
# Write a recursive function count_characters(items) that returns the total number of characters in all item names combined. For example, ["milk", "bread"] has 4 + 5 = 9 characters..


