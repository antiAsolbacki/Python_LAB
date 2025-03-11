import pyodbc
import argparse

def get_connection(server, database):
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error connecting to database: {sqlstate}")
        return None

def display_students(cursor):
    try:
        cursor.execute("SELECT SinhVien.ID, SinhVien.HoTen, Lop.TenLop FROM SinhVien LEFT JOIN Lop ON SinhVien.MaLop = Lop.ID")
        rows = cursor.fetchall()

        if rows:
            print("{:<5} {:<30} {:<20}".format("ID", "HoTen", "TenLop"))
            print("-" * 60)
            for row in rows:
                print("{:<5} {:<30} {:<20}".format(row.ID, row.HoTen, row.TenLop if row.TenLop else "N/A"))
        else:
            print("No students found.")

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error fetching data: {sqlstate}")
        print(ex)

def main():
    parser = argparse.ArgumentParser(description="Display student information from SQL Server.")
    parser.add_argument("--server", default="LAPTOP-AN51555\\LAPTOPAN51555", help="SQL Server hostname or IP address.")
    parser.add_argument("--database", default="QLSinhVien", help="Database name.")

    args = parser.parse_args()

    conn = get_connection(args.server, args.database)
    if conn:
        cursor = conn.cursor()
        display_students(cursor)
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()