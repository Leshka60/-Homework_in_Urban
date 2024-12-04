CREATE TABLE IF NOT EXISTS Test_Table(
    id INTEGER PRIMARY KEY,
    Author
    TEXT,
    Title
    TEXT,
    Publication INTEGER);



INSERT INTO Test_Table(Author, Title, Publication)
VALUES('Test1', 'qwertyu', 2022),
('Test2', 'asdfghj', 2023),
('Test3', 'zxcvbnm', 2024);

SELECT * FROM Test_Table;
