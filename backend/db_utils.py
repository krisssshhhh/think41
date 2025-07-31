import psycopg2

DB_CONFIG = {
    "dbname": "ecommerce_db",
    "user": "krishkumar",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def get_top_5_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT products.name, COUNT(*) AS total_sold
        FROM order_items
        JOIN products ON order_items.product_id = products.id
        WHERE order_items.status != 'Cancelled'
        GROUP BY products.name
        ORDER BY total_sold DESC
        LIMIT 5;
    """)
    result = cursor.fetchall()
    conn.close()
    return result


def get_order_status(order_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT status, shipped_at, delivered_at, returned_at
        FROM orders
        WHERE order_id = %s
    """, (order_id,))
    result = cursor.fetchone()
    conn.close()
    return result


def get_stock_for_product(product_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM inventory_items
        WHERE product_name ILIKE %s AND sold_at IS NULL
    """, (f"%{product_name}%",))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0