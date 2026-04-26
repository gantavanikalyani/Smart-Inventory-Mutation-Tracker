import copy

def create_inventory():
    inventory = [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "rating": 4.5}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "rating": 4.2}
        }
    ]
    return inventory

def apply_discount(data, roll_digit):
    n = len(data)
    index_to_modify = roll_digit % n

    for i in range(n):

        data[i]["details"]["price"] *= 0.9


        if i == index_to_modify:
            data[i]["details"]["stock"] -= 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i]["details"] == modified[i]["details"]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

roll_number = input("Enter your roll number: ")
last_digit = int(roll_number[-1])

inventory = create_inventory()

original_backup = copy.deepcopy(inventory)

shallow_copy = inventory.copy()
deep_copy = copy.deepcopy(inventory)

apply_discount(shallow_copy, last_digit)
apply_discount(deep_copy, last_digit)

shallow_result = compare_data(inventory, shallow_copy)
deep_result = compare_data(original_backup, deep_copy)

print("\nOriginal Inventory")
print(inventory)

print("\nShallow Copy")
print(shallow_copy)

print("\nDeep Copy")
print(deep_copy)

print("\nComparison")
print("Shallow Copy Changes (changed, unchanged):", shallow_result)
print("Deep Copy Changes (changed, unchanged):", deep_result)

print("\nAnalysis")
print("Shallow Copy: Changes affected original data because nested dictionaries share the same reference.")
print("Deep Copy: Changes did NOT affect original data because it creates a completely independent copy.")

print("\nExplanation")
print("In shallow copy, only the outer list is copied, but inner dictionaries are shared.")
print("So modifying copied data also changes the original inventory.")
print("In deep copy, all levels are copied, so original data remains unchanged.")