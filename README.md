# Smart-Inventory-Mutation-Tracker
## Problem Understanding

This program manages an inventory system where each product contains nested details such as price, stock, and rating. It creates copies of the inventory data and analyzes how changes affect the original data. The goal is to understand the difference between shallow copy and deep copy in Python. The program also compares the original and modified data to identify changes.

## Logic Used

The program uses a list of dictionaries to store inventory data. Functions are used to organize the logic into smaller parts.

create_inventory() → creates initial inventory
apply_discount(data) → reduces price by 10% and modifies stock
compare_data(original, modified) → compares data and counts changes

A shallow copy and a deep copy are created. Using loops and conditions, the program modifies the copied data and checks how it affects the original data. Finally, it displays the results and analysis.

## Personalization Applied

The program uses roll number-based logic to decide which item to modify.

Last digit of Register Number = Used
Index = last_digit % length of inventory

This ensures that only one specific item is modified based on the roll number, making the output unique for each user.

## Features
Uses lists and dictionaries (nested structure)
Implements multiple functions
Demonstrates shallow copy and deep copy
Applies mutation (price and stock changes)
Uses loops and conditional statements
Compares original and modified data
Provides analysis and explanation
Includes personalized logic based on roll number

## Learning Outcome

This project helped me understand how nested data structures work and how copying data affects the original structure. I learned the difference between shallow copy and deep copy through practical implementation.

It also improved my understanding of functions, loops, and conditional logic. Overall, this challenge enhanced my problem-solving skills and helped me understand real-world data handling scenarios.

## Conclusion

The program successfully demonstrates how data mutation works in different types of copies. It clearly shows that shallow copy shares references while deep copy creates independent data. This makes the program useful for understanding real-world data integrity issues.
