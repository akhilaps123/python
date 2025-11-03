def stationary_shop():
    user = input("Enter a new item:")
    import os
    if not os.path.exists("items.txt"):
        f = open("items.txt","w")
        f.write(user +"\n")
        f.close()
    else:
        f = open("items.txt","a")
        f.write(user +"\n")
        f.close()
    print("\nCurrent list of items:")
    with open("items.txt","r") as file:
        print(file.read())
stationary_shop()
# You are helping a small stationery shop owner manage a simple list of items.
# First, ask the user to enter the name of a new item.
# If the file items.txt does not exist, create it and write the item into it.
# If the file exists, open it in append mode and add the new item.
# After writing, display the full list of items from the file to the user