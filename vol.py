# A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
# The shop sold:
# 15.5 liters of apple juice
# 20 liters of orange juice
# 10.25 liters of grape juice
# Your task:
# Store the volume of each juice in separate variables.
# Calculate the total volume sold.
# Print the total volume.
# Convert the total volume to an integer and print it.
# Convert the total volume to a string and print it with a message.
# Add a random number between 5 and 10 (representing additional bonus liters) and print the final total
a,b,c = "apple","orange","grape"
apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25
total_volume = apple_juice + orange_juice + grape_juice
print(total_volume)
print(int(total_volume))
print("Total volume of juice sold is " + str(total_volume) + " liters")
import random
bonus_liters = random.randint(5,11)
print(+ total_volume + bonus_liters)

