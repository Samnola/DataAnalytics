-- 1) Write a query to list the product id, product name, and unit price of every product that Northwind sells. (Hint: To help set up your query, look at the schema preview to see what column names belong to each table. Or use SELECT * to query all columns first, then refine your query to just the columns you want.) */ 
SELECT ProductID,ProductName,UnitPrice
FROM products

-- 2) Write a query to identify the products where the unit price is $7.50 or less
SELECT ProductID,Productname,UnitPrice
FROM products
WHERE UnitPrice <= 7.50;

-- 3) What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question 
SELECT ProductID,Productname,UnitsInStock, UnitsOnOrder
FROM products 
WHERE UnitsInStock = 0 AND 
UnitsOnOrder > 0;

-- 4) Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories? Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry. 
-- The products table uses CategoryID to identify the category of each product. 
SELECT ProductID, ProductName, CategoryID
FROM products;
SELECT CategoryID, CategoryName
FROM categories;

SELECT p.ProductID, p.ProductName, c.CategoryName
FROM products AS p
INNER JOIN categories AS c
	ON p.CategoryID = c.CategoryID;

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM products AS p
INNER JOIN categories AS c
	ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood'
ORDER BY p.ProductName;

-- 5) Examine the products table again. How do you know what supplier each product comes from? Through the SupplierID
-- Where can you find info on suppliers? In the suppliers table.
-- Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.

SELECT SupplierID FROM suppliers 
WHERE CompanyName= 'Tokyo Traders' ; 

SELECT ProductName FROM products 
WHERE SupplierID= 4 ; 

-- 6) How many employees work at northwind? What employees have "manager" somewhere in their job title? Write queries to answer each question

SELECT COUNT(*) 
FROM employees 

SELECT LastName, FirstName
FROM employees
WHERE Title LIKE '%Manager%';


