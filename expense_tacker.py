import mysql.connector
print("MySQL connector is waiting!")
import csv

# --------- Database Configuration ---------
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345678',
    'database': 'expense_tracker'
}

# --------- Step 1: Get User Input ---------
amount = float(input("Enter amount: "))
category = input("Enter category: ")
date = input("Enter date (YYYY-MM-DD): ")

# --------- Step 2: Insert into MySQL ---------
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "INSERT INTO expenses (amount, category, date) VALUES (%s, %s, %s)"
    cursor.execute(query, (amount, category, date))
    conn.commit()
    print("✅ Data inserted into MySQL successfully.")
except Exception as e:
    print("❌ Error inserting into MySQL:", e)
finally:
    cursor.close()
    conn.close()

# --------- Step 3: Export to CSV ---------
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Amount", "Category", "Date"])
        writer.writerows(rows)
    print("✅ Data exported to CSV.")
except Exception as e:
    print("❌ Error exporting CSV:", e)
finally:
    cursor.close()
    conn.close()
