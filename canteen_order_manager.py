orders = []

for i in range(1, 6):
    orders.append(input(f"Enter Order {i}: "))

print("Original Orders: ")
print(orders)

orders.append(input("Enter additional order: "))
print("Updated Orders: ")
print(orders)

orders.insert(0, input("Enter priority order: "))
print("Updated Orders: ")
print(orders)

food = input("Search for an order: ")
if food in orders:
    count = orders.count(food)
    index = orders.index(food)
    print(f"Number of Occurrences: {count}")
    print(f"First Index: {index}")

else:
    print(f"Order '{food}' not found.")

cancel = input("Enter order to cancel: ")
orders.remove(cancel)
print("Updated Orders: ")
print(orders)
last_cancel = input("Last Order Removed: ")
to_pop = orders.index(last_cancel)
removed = orders.pop(to_pop)

print("\n===== FINAL ORDER REPORT =====")
orders.sort()
print(f"Orders: {orders}")
remaining = len(orders)
print(f"Total Remaining Orders: {remaining}")
