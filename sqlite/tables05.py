#!/usr/bin/python3
"""J. Hutcheson | Retrieving table data with SQLite"""

import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('my_database2.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Execute the SQL query to find the product associated with "XYZ Corp"
c.execute('''SELECT products.name
             FROM products
             WHERE company_id = (
                SELECT id
                FROM companies
                WHERE name = 'XYZ Corp.')''')

# Fetch the results of the query
result = c.fetchall()

# Print the result
# print(result)
print(result) # out results are returned to us in a tuple, uncomment out the above line if you'd like to see that.

# Close the database connection
conn.close()