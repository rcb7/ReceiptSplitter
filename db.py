import sqlite3

conn = sqlite3.connect('receiptSplitter.db')

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        ) 
    ''')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
        ) 
    ''')
    conn.commit()
    
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id INTEGER,
            total_amount REAL,
            date TEXT,
            payer_id INTEGER,
            FOREIGN KEY (payer_id) REFERENCES users (id)
        ) 
    ''')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL,
            quantity INTEGER,
            FOREIGN KEY (receipt_id) REFERENCES receipts (id)
        ) 
    ''')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS splits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_id INTEGER,
            item_id INTEGER,
            payer_id INTEGER,
            debtor_id INTEGER,
            amountOwed REAL,
            amountPaid REAL,
            FOREIGN KEY (item_id) REFERENCES items (id),
            FOREIGN KEY (debtor_id) REFERENCES users (id)
        ) 
    ''')
    conn.commit()
    
