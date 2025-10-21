# A grocery store wants to calculate the final bill for a customer. The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
# Rice: ?45 per kg
# Sugar: ?40 per kg
# Oil: ?130 per kg
# Assume a customer bought:
# 3 kg of rice
# 2.5 kg of sugar
# 1.8 kg of oil
# Your task:
# Use variables to store the prices and quantities.
# Use appropriate data types.
# Calculate and print the total price for each item and the final total bill.
# Show the total bill as an integer and also as a string.
# Convert the float values where needed using explicit conversion.
# Use random number generation to add a random ?5–?10 delivery charge.
# Show the final bill amount including delivery charge.



rice_price = 45 
sugar_price = 40
oil_price = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity =1.8

total_rice = rice_price * rice_quantity
total_sugar = sugar_price* sugar_quantity
total_oil = oil_price * oil_quantity
final_bill = total_rice + total_sugar + total_oil 
print("Total price for rice is : ", total_rice)
print("Total price for sugar is : ", total_sugar)
print("Total price for oil is : ", total_oil)
print ("final_bill is:" , final_bill)
print("final bill as an integer:", int(final_bill))
print("final bill as an string:" , str(final_bill))
import random
delivery_charge = random.randint(5,10)
print("deliver charge is :", delivery_charge)
final_amount = final_bill + delivery_charge
print("final amount including delivery charge is :", final_amount)



