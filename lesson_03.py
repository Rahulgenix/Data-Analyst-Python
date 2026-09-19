product = input("Enter product name:")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
discount_percent = float(input("Enter discount percentage: "))
total_amount = price * quantity
discount_amount = total_amount * (discount_percent / 100)
final_amount = total_amount - discount_amount         

print("\n ---bill---")
print("Product: ", product)
print("total_amount: ", total_amount)
print("discount_amount: ", discount_amount)
print("final_amount: ", final_amount)