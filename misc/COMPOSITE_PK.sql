select * from best_books_awards_2nf limit 10;

select * from best_books_characters_2NF limit 10;

select * from best_books_genres_2NF limit 10;

select * from best_books_ratingsByStars_2NF limit 10;

select * from best_books_setting_2NF limit 10;

select * from best_books_2NF limit 10;


-- Adding COMPOSITE PK to table best_books_2NF

ALTER TABLE best_books_2NF
DROP COLUMN id;

ALTER TABLE best_books_2NF
ADD COLUMN id INT GENERATED ALWAYS AS IDENTITY UNIQUE;

ALTER TABLE best_books_2NF
ADD PRIMARY KEY(id, book_id);


ALTER TABLE best_books_awards_2nf
ADD COLUMN best_books_id REFERENCES best_books_2nf ()