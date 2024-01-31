import psycopg2


class db_operations:


    def __init__(self):
        print("Class dboperations")
    
    def establish_connection(self):
       conn = psycopg2.connect(database="facts_db", user="postgres", password="admin123", host="127.0.0.1",
                                port="5432")
       return conn
    
    def insert_data(self,data):
        conn = self.establish_connection()
        cur = conn.cursor()
        try:
            for row in data:
                fact = row[0]
                # Using parameterized queries
                cur.execute(f"INSERT INTO facts_table (facts) VALUES ('{fact}')")
            conn.commit()  # Commit changes to the database
        except Exception as e:
            # Handle exceptions, such as database errors
            print("Error inserting data:", e)
            conn.rollback()  # Rollback changes if an error occurs
        finally:
            cur.close()  # Close cursor
            conn.close()  # Close connection 

    def fetch_fact(self):
        conn = self.establish_connection()
        cur = conn.cursor()
        cur.execute("SELECT (facts) from facts_table ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchone()
        fact = row[0]
        conn.commit()
        conn.close()
        return fact