import psycopg2

conn = psycopg2.connect(
    dbname="ecommerce_db",
    user="krishkumar",  # or postgres
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);
""")

# Create Chat Sessions
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_sessions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Create Messages
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    session_id INT REFERENCES chat_sessions(id),
    sender TEXT CHECK (sender IN ('user', 'ai')),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cursor.close()
conn.close()

print("✅ Chat schema created successfully.")