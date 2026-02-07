import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')


# First 10 rows of the orderdetails and products tables joined on productCode
q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
print(pd.read_sql(q, conn))
print("\n")


# First 10 rows of the orderdetails table
q = """
SELECT *
 FROM orderdetails
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
print("\n")


# First 10 rows of the products table
q = """
SELECT *
 FROM products
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
print("\n")


# First 10 rows of the orderdetails table joined with products using USING clause
q = """
SELECT *
 FROM orderdetails
   JOIN products
     USING(productCode)
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
print("\n")


# First 10 rows of the orderdetails table joined with products using table aliases
q = """
SELECT *
 FROM orderdetails AS od
   JOIN products AS p
     ON od.productCode = p.productCode
 LIMIT 10;
"""
print(pd.read_sql(q, conn))
print("\n")


# All records from products and matching records from orderdetails using LEFT JOIN
q = """
SELECT *
 FROM products
   LEFT JOIN orderdetails
     USING(productCode);
"""
df = pd.read_sql(q, conn)
print("Number of records returned:", len(df))
print("\n")
print("Number of records where order details are null:", len(df[df.orderNumber.isnull()]))
print("\n")
print(df[df.orderNumber.isnull()])
print("\n")


# All records from orderdetails and matching records from products using Inner JOIN and table aliases
q = """
SELECT *
 FROM customers AS c
      JOIN employees AS e
      ON c.salesRepEmployeeNumber = e.employeeNumber
      ORDER By employeeNumber;
"""
print(pd.read_sql(q, conn))
print("\n")

conn.close()