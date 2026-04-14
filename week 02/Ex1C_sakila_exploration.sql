/*
a) In the column section under actor you will find: actor id, first name, last name and last update.
b) In the "film" column section you will find: film id, title, description, release year, language id, original language id, rental duration, rental rate, length, replacement cost, rating, special features and last update. 
c) Film actor is the only other column that contains actor id and fil id. 
d) This table included information such as: rental id, rental date, inventory id, customer id, return date, staff id and last update. This information was pretty straightforward and easy to read. While it may be an overwhelming amount of information it is easy to read. 
e) The table for inventory includes the following information: inventory id, film id, store id and last update. 
f) To find the names of all films rented on a specific date, you would need to use the rental, inventory and film tables. The rental table contains the rental daye and inventory id, which connects the inventory table. 

*/
SELECT rental_date, inventory_id 
FROM rental;
SELECT film_id, title
FROM film;

