import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Read CSVs
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")
products = pd.read_csv("data/products.csv")
inventory = pd.read_csv("data/inventory_items.csv")

# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    status TEXT,
    gender TEXT,
    created_at TIMESTAMP,
    returned_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    num_of_item INT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id BIGINT PRIMARY KEY,
    cost FLOAT,
    category TEXT,
    name TEXT,
    brand TEXT,
    retail_price FLOAT,
    department TEXT,
    sku TEXT,
    distribution_center_id BIGINT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id BIGINT PRIMARY KEY,
    order_id BIGINT,
    user_id BIGINT,
    product_id BIGINT,
    inventory_item_id BIGINT,
    status TEXT,
    created_at TIMESTAMP,
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    returned_at TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory_items (
    id BIGINT PRIMARY KEY,
    product_id BIGINT,
    created_at TIMESTAMP,
    sold_at TIMESTAMP,
    cost FLOAT,
    product_category TEXT,
    product_name TEXT,
    product_brand TEXT,
    product_retail_price FLOAT,
    product_department TEXT,
    product_sku TEXT,
    product_distribution_center_id BIGINT
);
""")

conn.commit()

# Insert data using COPY (better performance)
def load_table(df, table_name):
    print(f"Inserting into {table_name}...")
    df.to_csv(f"{table_name}.csv", index=False)
    with open(f"{table_name}.csv", 'r') as f:
        next(f)  # skip header
        cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", f)
    conn.commit()

load_table(orders, "orders")
load_table(products, "products")
load_table(order_items, "order_items")
load_table(inventory, "inventory_items")

cursor.close()
conn.close()
print("✅ All data loaded into PostgreSQL.")