-- 1. GET every rows and all columns from the Table products
-- SELECT * FROM products;

-- 2. GET specific columns from the table
-- SELECT id, name, price FROM products;

-- 3. Rename a specific column
-- SELECT id AS product_id FROM products;

-- 4. WHERE statement
-- SELECT * FROM products WHERE inventory=0;

-- 5. WHERE statement for name column, means you need to add quotation marks
-- SELECT * FROM products WHERE name = 'DVD Player';

-- 6. ALL ITEMS WHERE PRICE > 50
-- SELECT * FROM products WHERE price <=100;

-- 7. NOT operator '<>' or '!='
-- SELECT * FROM products WHERE inventory <> 0;

-- AND STATEMENT
-- SELECT * FROM products WHERE price >= 50 AND inventory > 0;

-- OR statement
-- SELECT * FROM products WHERE price >= 25 OR inventory >= 1

-- IN operator allows to add a list
-- SELECT * FROM products WHERE id IN (1, 2, 3)

-- LIKE operator -> use the %-sign before or after the letters/text
-- SELECT * FROM products WHERE name NOT LIKE '%E%'

-- FILTER BASED ON PRICE -- ORDER BY
-- SELECT * FROM products ORDER BY price DESC;

-- ORDER BY while selecting certain column
-- SELECT * FROM products ORDER BY inventory DESC, price DESC;

-- order by created_at -> if you do DESC, that means largest first, so most recent
-- if you do ASC, that means the order of their creation
-- ORDER BY is ASC by default
-- SELECT * FROM products WHERE price >= 20 ORDER BY created_at ASC;

-- LIMIT keyword
-- SELECT * FROM products WHERE price >= 5 LIMIT 15;

-- OFFSET keyword -> SKIPPING CERTAIN ROWS
-- SELECT * FROM products ORDER BY id LIMIT 5 OFFSET 5;

-- CREATING A NEW PRODUCT
-- INSERT INTO products (name, price, inventory) VALUES('tortilla', 4, 300)

-- SELECT * FROM products;

-- RETURNING for getting back stuff
-- INSERT INTO products (name, price, inventory) VALUES('laptop', 900, 7), ('mouse', 55, 23), ('mat', 15, 10) returning *;

-- DELETE keyword
-- DELETE FROM products WHERE id=11 RETURNING *;

-- DELETE WHERE inventory = 0
-- DELETE FROM products WHERE inventory = 0;

-- UPDATE an entry
-- UPDATE products SET name = 'coca cola', price = 3 WHERE id = 14 returning *;

-- UPDATE one column for a row
-- UPDATE products SET is_sale = true WHERE id = 15 RETURNING *;

-- UPDATING multiple rows:
-- UPDATE products SET is_sale = true RETURNING *;

