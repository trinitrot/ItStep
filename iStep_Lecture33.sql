-- 0. create database

Create database books;

-- 1. create table

CREATE TABLE books (
    id            SERIAL,
    title         VARCHAR(150) NOT NULL,
    author        VARCHAR(100) NOT NULL,
    genre         VARCHAR(50),
    publish_year  INTEGER,
    pages         INTEGER,
    price         NUMERIC(8, 2)
);

-- 2. insert data

INSERT INTO books (title, author, genre, publish_year, pages, price) VALUES
    ('The Hobbit',                               'J.R.R. Tolkien',     'Fantasy',         1937, 310, 32.50),
    ('1984',                                     'George Orwell',      'Dystopian',       1949, 328, 24.90),
    ('Harry Potter and the Philosopher''s Stone','J.K. Rowling',       'Fantasy',         1997, 223, 29.99),
    ('The Name of the Wind',                     'Patrick Rothfuss',   'Fantasy',         2007, 662, 42.00),
    ('Project Hail Mary',                        'Andy Weir',          'Science Fiction', 2021, 476, 38.50),
    ('Dune',                                     'Frank Herbert',      'Science Fiction', 1965, 412, 35.00),
    ('Sapiens',                                  'Yuval Noah Harari',  'History',         2011, 443, 36.00),
    ('Atomic Habits',                            'James Clear',        'Self-help',       2018, 320, 27.50),
    ('The Midnight Library',                     'Matt Haig',          'Fiction',         2020, 288, 26.00),
    ('Fourth Wing',                              'Rebecca Yarros',     'Fantasy',         2023, 528, 45.00),
    ('Crime and Punishment',                     'Fyodor Dostoevsky',  'Classic',         1866, 671, 22.00),
    ('The Da Vinci Code',                        'Dan Brown',          'Thriller',        2003, 489, 28.00),
    ('Tomorrow, and Tomorrow, and Tomorrow',     'Gabrielle Zevin',    'Fiction',         2022, 416, 33.00),
    ('დათა თუთაშხია',                            'ჭაბუა ამირეჯიბი',    'Novel',           1975, 750, 34.00),
    ('Clean Code',                               'Robert C. Martin',   'Programming',     2008, 464, 55.00);

-- 3. Select

SELECT * FROM books;

SELECT title, author FROM books;

SELECT * FROM books
WHERE price > 30;

SELECT * FROM books
WHERE publish_year >= 2020;

SELECT * FROM books
WHERE genre = 'Fantasy';

SELECT * FROM books
WHERE pages > 300;

SELECT * FROM books
ORDER BY price;

SELECT * FROM books
ORDER BY publish_year DESC;

-- 4. update

UPDATE books
SET price = 40
WHERE id = 5;

UPDATE books
SET genre = 'Fantasy'
WHERE id = 9;

UPDATE books
SET pages = 498
WHERE id = 7;

-- 5. delete

DELETE FROM books
WHERE id = 12;

DELETE FROM books
WHERE publish_year < 2000;

-- 6. insert rows

INSERT INTO books (title, author, genre, publish_year, pages, price) VALUES
    ('The Way of Kings',   'Brandon Sanderson', 'Fantasy',   2010, 1007, 48.00),
    ('Klara and the Sun',  'Kazuo Ishiguro',    'Fiction',   2021,  303, 31.00),
    ('Iron Flame',         'Rebecca Yarros',    'Fantasy',   2023,  623, 46.50),
    ('Deep Work',          'Cal Newport',       'Self-help', 2016,  296, 29.00),
    ('Educated',           'Tara Westover',     'Memoir',    2018,  334, 30.50);

-- 7. select all

SELECT * FROM books;

-- 8. delete table

DROP TABLE books;
