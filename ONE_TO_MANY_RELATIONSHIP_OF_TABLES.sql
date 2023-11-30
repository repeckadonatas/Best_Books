select * from best_books_awards_2nf limit 100;

select * from best_books_2NF limit 10;


select * from best_books_genres_2NF limit 100;

select * from best_books_characters_2NF limit 100;


select * from best_books_2nf
where series like '%The Hunger Games%';


-- Creating a table to act as connection between other tables

CREATE TABLE book_id AS
SELECT book_id
FROM best_books_2nf
GROUP BY book_id;

select * from book_id;

ALTER TABLE book_id
ADD PRIMARY KEY(book_id);


-- Adding PK to tables without it

-- best_books_awards_2NF
ALTER TABLE best_books_awards_2NF
ADD COLUMN unique_id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_awards_2NF
ADD PRIMARY KEY (unique_id);


-- best_books_characters_2nf
ALTER TABLE best_books_characters_2nf
ADD COLUMN unique_id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_characters_2nf
ADD PRIMARY KEY (unique_id);


-- best_books_genres_2nf
ALTER TABLE best_books_genres_2nf
ADD COLUMN unique_id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_genres_2nf
ADD PRIMARY KEY (unique_id);


-- best_books_ratingsByStars_2nf
ALTER TABLE best_books_ratingsByStars_2nf
ADD COLUMN unique_id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_ratingsByStars_2nf
ADD PRIMARY KEY (unique_id);


-- best_books_setting_2nf
ALTER TABLE best_books_setting_2nf
ADD COLUMN unique_id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_setting_2nf
ADD PRIMARY KEY (unique_id);



select * from best_books_awards_2NF;

-- Adding FK constraints to tables

ALTER TABLE best_books_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


ALTER TABLE best_books_awards_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


ALTER TABLE best_books_characters_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


ALTER TABLE best_books_genres_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


ALTER TABLE best_books_ratingsByStars_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


ALTER TABLE best_books_setting_2nf 
ADD FOREIGN KEY (book_id) 
REFERENCES book_id (book_id)
ON DELETE CASCADE;


select * from best_books_awards_2nf LIMIT 20;



--JOIN to check the relationships between tables

SELECT 
book_id.book_id as book_id,
best_books_2NF.title as title,
best_books_awards_2NF.awards as awards

FROM book_id, best_books_2NF, best_books_awards_2NF

INNER JOIN book_id title ON book_id.book_id = title.book_id
INNER JOIN book_id awards ON book_id.book_id = awards.book_id;

