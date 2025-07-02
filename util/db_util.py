import pyodbc

class DBUtil:
    @staticmethod
    def get_connection():
        try:
            conn_str = (
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=localhost;"
                "Database=HMBank;"
                "Trusted_Connection=yes;"
            )
            return pyodbc.connect(conn_str)
        except pyodbc.Error as e:
            return None

if __name__ == "__main__":
    conn = DBUtil.get_connection()
    if conn:
        print("Connected successfully")
        conn.close()
    else:
        print("Connection failed.")
