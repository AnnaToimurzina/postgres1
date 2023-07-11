-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  first_name varchar(50),
  last_name varchar(50),
  birthday DATE,
  phone varchar(20)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name


-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE users
RENAME COLUMN birthday TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE table_name ALTER COLUMN phone TYPE varchar(32);


-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birthday, phone)
VALUES ('John', 'Doe', '1995-05-10', '1234567890');

INSERT INTO student (first_name, last_name, birthday, phone)
VALUES ('Jane', 'Smith', '1998-08-20', '0987654321');

INSERT INTO student (first_name, last_name, birthday, phone)
VALUES ('Michael', 'Johnson', '1993-02-15', '9876543210');


-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student
