#Project-for-Python-essential-course
#Inventory management system by achyutam sharma 26bce10159

Inventory Management System

Python Essentials Course Project

Author: Achyutam Sharma
Student ID: 26BCE10159

________________

Project Overview

The Inventory Management System is a Python application which is designed to manage products in an inventory.

This program allows users to
add products, 
view stored products, 
search for a product using its index, 
update product information,
sell products, 
and delete products from the inventory.

This project is developed as part of the Python Essentials Course and it demonstrate fundamental Python programming concepts such as dictionaries, functions, loops, conditional statements, user input, and basic data management.

________________

Features

The system provides the following options:

1. Add New Product
   
   - Add a product to the inventory.
   - Store the product's name, quantity, and price.

2. View All Products
   
   - Display all products currently stored in the inventory.

3. Search a Product
   
   - Search for a product using its inventory index.

4. Update Product
   
   - Update the:
     - Product name
     - Product quantity
     - Product price

5. Sell a Product

   - Decrease the product quantity by one.

6. Delete a Product
   
   - Remove a product from the inventory.

7. Exit
   
   - Exit the application with a closing message.

________________

Tools and Technologies Used

- Programming Language: Python
- Data Structure: Dictionary
- Development Environment: Any Python-compatible IDE or code editor
- Input/Output: Python "input()" and "print()" functions

Python Concepts Used

- Variables
- Dictionaries
- Functions
- "if" statements
- "while" loops
- "for" loops
- User input
- Type conversion using "int()"
- Dictionary operations
- Basic CRUD operations

________________

Project Structure

Project-for-Python-essential-course/

1.project.py
2.README.md
3.statement.md

________________

Installation

1. Install Python

Download and install Python from the official Python website and Verify the installation

2. Clone the Repository

If the project is hosted on GitHub, clone it using:

git clone <repository-url>

Then navigate to the project directory:

cd Project-for-Python-essential-course

3. No External Libraries Required

This project uses only Python's built-in functionality. Therefore, no external packages or dependencies need to be installed.

________________

How to Run

Open a terminal inside the project directory and run:

python inventory.py

The program will display the Inventory Management System menu.

---

How to Use

After starting the program, the following menu is displayed:

1. Add new product
2. View all products
3. Search a product
4. Update product
5. Sell a product
6. Delete a product
7. Exit

Enter the number corresponding to the operation you want to perform.

Example: Adding a Product

Select option "1" and enter the requested information:

enter your choice: 1

Adding new product

enter product's name: Laptop
enter product's quantity: 5
enter product's price: 50000

The product is then stored in the inventory.

________________

Testing Instructions

The program can be tested by checking each menu option individually.

Test 1: Add Product

1. Select option "1".
2. Enter a product name.
3. Enter its quantity.
4. Enter its price.
5. Select option "2" to verify that the product was added.

Expected result: The newly added product should be displayed.

---

Test 2: View Products

1. Add one or more products.
2. Select option "2".

Expected result: All currently stored products should be displayed.

---

Test 3: Search Product

1. Add a product.
2. Note its index.
3. Select option "3".
4. Enter the product's index.

Expected result: The corresponding product information should be displayed.

You can also enter an index that does not exist.

Expected result: The program should display no product on this index

---

Test 4: Update Product

1. Add a product.
2. Select option "4".
3. Enter the product index.
4. Choose whether to update the name, quantity, or price.
5. Enter the new value.

Expected result: The selected product information should be updated.

---

Test 5: Sell Product

1. Add a product with a quantity greater than zero.
2. Select option "5".
3. Enter the product index.

Expected result: The product quantity should decrease by one.

---

Test 6: Delete Product

1. Add a product.
2. Select option "6".
3. Enter the product index.

Expected result: The selected product should be removed from the inventory.

---

Test 7: Exit

1. Select option "7".

Expected result: The program should display the closing message and terminate the menu operations.

________________

Author

Achyutam Sharma
Student ID: 26BCE10159

Course: Python Essentials


