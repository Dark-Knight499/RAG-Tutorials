import sqlite3
import random
import datetime

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email TEXT UNIQUE NOT NULL,
        Password TEXT NOT NULL,
        Address TEXT,
        PhoneNumber TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY,
        ProductName TEXT NOT NULL,
        Description TEXT,
        Price REAL NOT NULL,
        StockQuantity INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY,
        CustomerID INTEGER,
        OrderDate TEXT,
        TotalAmount REAL NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS OrderItems (
        OrderItemID INTEGER PRIMARY KEY,
        OrderID INTEGER,
        ProductID INTEGER,
        Quantity INTEGER NOT NULL,
        Price REAL NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY,
        CategoryName TEXT UNIQUE NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ProductCategories (
        ProductID INTEGER,
        CategoryID INTEGER,
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
        PRIMARY KEY (ProductID, CategoryID)
    )
''')

# Sample data
first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
last_names = ['Smith', 'Jones', 'Williams', 'Brown', 'Davis']
product_names = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch']
categories = ['Electronics', 'Books', 'Home & Kitchen', 'Clothing', 'Sports']

# Function to generate a random date between two dates
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime('%Y-%m-%d')

# Generate and insert dummy data
num_customers = 10
num_products = 20
num_orders = 30

# Insert categories
for category_name in categories:
    cursor.execute('''INSERT INTO Categories (CategoryName) VALUES (?)''', (category_name,))

# Insert customers
for i in range(num_customers):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f'{first_name.lower()}.{last_name.lower()}{i}@example.com'
    password = 'password123'  # In real scenarios, hash the password
    address = f'{random.randint(1, 100)} Main St'
    phone_number = f'555-{random.randint(100, 999)}-{random.randint(1000, 9999)}'

    cursor.execute('''
        INSERT INTO Customers (FirstName, LastName, Email, Password, Address, PhoneNumber)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, password, address, phone_number))

# Insert products
for i in range(num_products):
    product_name = f'{random.choice(product_names)} {i+1}'
    description = f'This is a sample product {i+1}'
    price = round(random.uniform(50, 2000), 2)
    stock_quantity = random.randint(10, 100)

    cursor.execute('''
        INSERT INTO Products (ProductName, Description, Price, StockQuantity)
        VALUES (?, ?, ?, ?)
    ''', (product_name, description, price, stock_quantity))

    product_id = cursor.lastrowid
    category_id = random.choice(range(1, len(categories) + 1))  # Category IDs start from 1

    cursor.execute('''
        INSERT INTO ProductCategories (ProductID, CategoryID)
        VALUES (?, ?)
    ''', (product_id, category_id))

# Insert orders
for i in range(num_orders):
    customer_id = random.randint(1, num_customers)
    order_date = random_date(datetime.date(2023, 1, 1), datetime.date(2024, 1, 1))
    total_amount = round(random.uniform(100, 5000), 2)

    cursor.execute('''
        INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
        VALUES (?, ?, ?)
    ''', (customer_id, order_date, total_amount))

    order_id = cursor.lastrowid
    num_items = random.randint(1, 5)

    for j in range(num_items):
        product_id = random.randint(1, num_products)
        quantity = random.randint(1, 3)
        # Fetch the price of the product
        cursor.execute('''SELECT Price FROM Products WHERE ProductID = ?''', (product_id,))
        product_price = cursor.fetchone()[0]
        item_price = product_price * quantity

        cursor.execute('''
            INSERT INTO OrderItems (OrderID, ProductID, Quantity, Price)
            VALUES (?, ?, ?, ?)
        ''', (order_id, product_id, quantity, item_price))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dummy ecommerce database created successfully!")