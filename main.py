from pickle import TRUE
import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='root', host='localhost')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
dbname = input("Enter database name: ")

# Doping database MYDATABASE if already exists
cursor.execute(f"DROP database IF EXISTS {dbname}")

# Creating a database with table from user input
cursor.execute(f"CREATE database {dbname}")
cursor.execute(f"USE {dbname}")
tbname = input("Enter table name: ")
cursor.execute(
    f"CREATE TABLE {tbname} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, reg_no VARCHAR(255))")
# Taking and adding data for the table from user
while TRUE:
    reply = input("Type Q to quit or enter to continue: ").lower()
    if reply == "q":
        break
    else:
        sql = f"INSERT INTO {tbname} (name, age, reg_no) VALUES (%s, %s, %s)"
        val = tuple(
            input('Enter Name, Age and Register Number in order: ').split())
        try:
            # Executing the SQL command
            cursor.execute(sql, val)

            # Commit your changes in the database
            conn.commit()

        except:
            # Rolling back in case of error
            conn.rollback()


# Retrieving the list of databases
print("\nList of data:\n ")
print(" ID--NAME--AGE--REG.NO\n")

# Printing the data in order with a loop
cursor.execute(f"SELECT * FROM {tbname}")
for x in cursor:
    print(x)

# Closing the connection
conn.close()

# For the terminal to stay open
input()
