sales = float(input("Enter sales amount: "))
rating = float(input("Enter rating (1-5): "))

if sales >= 100000 and rating >=4:
    print("excellent performance!")
else:
    print("needs improvement.")