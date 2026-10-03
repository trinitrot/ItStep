--===============================
-- Normalized DB creation
--===============================

CREATE TABLE customers (
    id     INT PRIMARY KEY,
    name   VARCHAR(100)  NOT NULL,
    phone  varchar(20),
    email  VARCHAR(100)
);

create TABLE categories (
    id    INT  PRIMARY KEY,
    name  VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    id            INT PRIMARY KEY,
    product_name  VARCHAR(100) not null,
    price         DECIMAL(10, 2)  NOT NULL,
    category_id   INT NOT NULL,
    FOREIGN KEY (category_id)  REFERENCES categories(id)
);

CREATE  TABLE orders (
    id           int PRIMARY KEY,
    customer_id  INT NOT NULL,
    order_date   DATE NOT NULL,
    foreign key (customer_id) REFERENCES customers(id)
);

CREATE TABLE ordered_items (
    order_id    INT NOT NULL,
    product_id  INT  NOT NULL,
    quantity    INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id)   REFERENCES orders(id),
    FOREIGN KEY (product_id) references products(id)
);

--=======================
-- Insedt data
--=======================

INSERT INTO customers (id, name, phone, email) VALUES
    (1, 'გიორგი ბერიძე',   '555111111', 'giorgi@mail.com'),
    (2, 'ნინო კაპანაძე',   '555222222', 'nino@mail.com'),
    (3, 'ლევან გელაშვილი', '555333333', 'levan@mail.com');

insert into categories (id, name) VALUES
    (1, 'Electronics'),
    (2, 'Furniture');

INSERT INTO  products (id, product_name, price, category_id) values
    (1, 'Laptop',   3200, 1),
    (2, 'Mouse',      80, 1),
    (3, 'Keyboard',  150, 1),
    (4, 'Chair',     420, 2),
    (5, 'Desk',      850, 2),
    (6, 'Monitor',   900, 1);

INSERT INTO orders (id, customer_id, order_date)  VALUES
    (1, 1, '2026-06-01'),
    (2, 2, '2026-06-03'),
    (3, 3, '2026-06-05'),
    (4, 1, '2026-06-10');

INSERT into ordered_items (order_id, product_id, quantity) VALUES
    (1, 1, 1),
    (1, 2, 2),
    (2, 3, 1),
    (3, 4, 4),
    (3, 5, 1),
    (4, 6, 2);

--==============
-- Joins
--==============

-- 1. შეკვეთების სრული ინფორმაცია
SELECT
    o.id,
    c.name,
    c.email,
    p.product_name,
    p.price,
    oi.quantity,
    o.order_date
FROM orders o
JOIN customers c  ON c.id = o.customer_id
JOIN ordered_items oi ON oi.order_id = o.id
join products p    ON p.id = oi.product_id;


-- 2. მომხმარებლების და მათი პროდუქტების სია
select
    c.name,
    p.product_name
FROM customers c
JOIN orders o      ON c.id = o.customer_id
JOIN ordered_items oi ON o.id  = oi.order_id
JOIN products p    on p.id = oi.product_id;


-- 3. პროდუქტების სია და მათი მყიდველები
SELECT
    p.product_name,
    p.price,
    c.name
FROM  products p
JOIN ordered_items oi ON p.id = oi.product_id
JOIN orders o      ON o.id = oi.order_id
JOIN customers c   ON c.id = o.customer_id;


-- 4. შეკვეთის დეტალები
SELECT
    o.id,
    c.name,
    p.product_name,
    oi.quantity,
    o.order_date
from orders o
JOIN customers c   ON c.id = o.customer_id
JOIN ordered_items oi  ON oi.order_id = o.id
JOIN products p    ON p.id = oi.product_id;


-- 5. პროდუქტი და მისი კატეგორია
SELECT
    p.product_name,
    cat.name
FROM products p
JOIN categories cat ON cat.id = p.category_id;


-- 6. Electronics კატეგორიის პროდუქტები
SELECT
    p.product_name,
    cat.name,
    p.price
FROM products p
join categories cat ON cat.id = p.category_id
WHERE cat.name = 'Electronics';


-- 7. კონკრეტული მომხმარებლის (გიორგი ბერიძე) შეკვეთები
SELECT
    o.id,
    c.name,
    p.product_name,
    oi.quantity
FROM customers c
JOIN orders o      ON c.id = o.customer_id
JOIN ordered_items oi ON o.id = oi.order_id
JOIN products p    ON p.id =  oi.product_id
where c.name = 'გიორგი ბერიძე';


-- 8. 2026-06-05-ს გაკეთებული შეკვეთები
SELECT
    o.order_date,
    c.name,
    p.product_name,
    oi.quantity
FROM orders o
JOIN customers c   ON c.id = o.customer_id
JOIN ordered_items oi ON o.id = oi.order_id
JOIN products p    ON p.id = oi.product_id
WHERE o.order_date = '20260605';


-- 9. მომხმარებლების სრული შესყიდვების ისტორია
SELECT
    c.name,
    c.email,
    p.product_name,
    oi.quantity
FROM customers c
JOIN orders o      ON c.id = o.customer_id
JOIN  ordered_items oi ON o.id = oi.order_id
JOIN products p    ON p.id = oi.product_id;


-- 10. პროდუქტები, რომლებიც ერთზე მეტი რაოდენობით არის შეძენილი
SELECT
    c.name,
    p.product_name,
    oi.quantity
FROM ordered_items oi
JOIN orders o    ON o.id = oi.order_id
JOIN customers c ON c.id = o.customer_id
JOIN products p  on p.id = oi.product_id
WHERE oi.quantity  > 1;
