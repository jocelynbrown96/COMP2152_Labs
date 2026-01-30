import math
# COMP2152 Open Source Development Lab 3: Friday January 30th, 2026
# Jocelyn Brown, Student Number: 101597391

# Question 1: Student Grades List (Lists - Basic Operations)

# Initial grades:
grades = [85, 92, 78, 95, 88]

# Add a new grade to the list:
grades.append(90)

# Sort the grades in ascending order:
grades.sort()

# Print results as per the given expected output:
print("Sorted grades:", grades) # sorted list
print("Highest grade:", grades[-1])  # last element using negative indexing
print("Lowest grade:", grades[0])    # first element
print("Total number of grades:", len(grades)) # total number of grades using len() function

# Question 2: Shopping Cart (Lists - Searching and Removal)

# Shopping cart items:
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

# Count and print the number of times "apple" appears in the cart:
print("Number of apples:", cart.count("apple"))

# Find position of "milk" in the cart and print the result:
print("Position of milk:", cart.index("milk"))

# Remove one "apple" from the cart:
cart.remove("apple")

# Pop last item from the cart and print the result:
removed_item = cart.pop()
print("Removed item using pop:", removed_item)

# Check if "banana" is in the cart and print the result:
print("Is banana in cart?", "banana" in cart)

# Print the final cart:
print("Final cart:", cart)

# Question 3: Coordinate System (Tuples - Creation and Unpacking)

# Tuples for points, point1 and point2 with given coordinates:
point1 = (3, 5)
point2 = (7, 2)

# Unpacking points into variables x1, y1 and x2, y2:
x1, y1 = point1
x2, y2 = point2

# Calculate distance between the points using the distance formula:
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create a tuple from the string "PYTHON" using the tuple() constructor:
chars_tuple = tuple("PYTHON")

# Print results as per the given expected output:
print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
print("Characters tuple:", chars_tuple)

# Print each character from the tuple using a for loop:
for char in chars_tuple:
    print(char)

# Question 4: Class Attendance (Sets - Uniqueness and Operations)

# Attendance sets:
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

# Add new student "Grace" to Monday class:
monday_class.add("Grace")

# Find students who attended both classes using intersection:
both_classes = monday_class & wednesday_class

# Find students who attended either class using union:
either_class = monday_class | wednesday_class

# Find students who attended only on Monday using difference:
only_monday = monday_class - wednesday_class

# Find students who attended only one class (not both) using symmetric difference:
only_one_class = monday_class ^ wednesday_class

# Check if monday_class is a subset of the union:
is_subset = monday_class <= either_class

# Print results as per the given expected output:
print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both_classes)
print("Attended either class:", either_class)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one_class)
print("Is Monday subset of all students?", is_subset)

# Question 5: Contact Book (Dictionaries - Basic Operations)

# Contact dictionary:
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

# Print Alice's number by accessing the dictionary:
print("Alice's number:", contacts["Alice"])

# Add "Diana" as a new contact:
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

# Update "Bob"'s number:
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

# Delete "Charlie" from contacts:
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

# Print all contact names, numbers, and total number of contacts:
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))

# Question 6: Inventory Management System (Combined - All Collections)

# Inventory dictionary:
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# Print current inventory using a for loop:
print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")

# Product categories using sets:
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
# Find all products using union and print the results:
all_products = electronics | accessories
print("\nAll product categories:", all_products)

# Price list from the inventory:
prices = [price for price, qty in inventory.values()]
print("\nPrice list:", prices)

# Sort prices and print the lowest and highest prices:
prices.sort()
print("Sorted prices:", prices)
print("Lowest price: $", prices[0])
print("Highest price: $", prices[-1])

# Add new product "Headphones" to the inventory:
inventory["Headphones"] = (49.99, 20)

# Update quantity of "Mouse" stock:
inventory["Mouse"] = (29.99, 12)

# Remove product "Monitor" from the inventory:
del inventory["Monitor"]

# Print the final inventory with formatted output:
print("\n=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")