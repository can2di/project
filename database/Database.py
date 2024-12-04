import sqlite3


class Database:
    def __init__(self, db_file):
        with sqlite3.connect(db_file) as conn:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()

        # Create the expenses table if it doesn't exist
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Spending (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount TEXT NOT NULL,
                category TEXT NOT NULL,  
                description TEXT NOT NULL
            )
        ''')
        
            self.conn.commit()
                

    def load_data(self, type, amount, category, description):
        try:
            self.conn = sqlite3.connect('expenses.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("INSERT INTO Spending (type, amount, category, description) VALUES (?, ?, ?, ?)", (type, amount, category, description))
            self.conn.commit()
            print("Data inserted successfully")
        except sqlite3.Error as error:
            print("Error inserting data:", error)
            self.close_connection() 
        self.close_connection() 


    def read_data(self):
        try:
            self.conn = sqlite3.connect('expenses.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM Spending")
            rows = self.cursor.fetchall()
            for row in rows:
                print("Id:", row[0])
                print("Type:", row[1])
                print("Amount:", row[2])
                print("Category:", row[3])
                print("Description:", row[4])
                print("\n")
        except sqlite3.Error as error:
            print("Error reading data:", error)
        self.close_connection()

    def fetch_all_data(self):
        self.conn = sqlite3.connect('expenses.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Spending")
        return self.cursor.fetchall()

    def delete_table(self, table_name):
        try:
            self.conn = sqlite3.connect('expenses.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"DROP TABLE {table_name}")
            self.conn.commit()
            print("Table deleted successfully")
        except sqlite3.Error as error:
            print("Error deleting table:", error)
        self.close_connection()

    def sort_data(self, sort_by='amount', order='ASC'):
        # if request.method == 'POST':
            query = f"SELECT * FROM Spending ORDER BY {sort_by} {order}"
            self.cursor.execute(query)
            return self.cursor.fetchall()
    
    def get_expense_by_id(self, id):
        query = "SELECT * FROM Spending WHERE id=?"
        self.cursor.execute(query, (id,))
        print(id)
        result = self.cursor.fetchone()
        print(result)
        return result
    
    def delete_expense(self, id):
        query = "DELETE FROM Spending WHERE id=?"
        self.cursor.execute(query, (id,))
        print(id)
        self.conn.commit()
        self.close_connection()

    def close_connection(self):
        self.conn.close()