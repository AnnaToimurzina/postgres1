import psycopg2
import csv



def main():
        """Скрипт для заполнения данными таблиц в БД Postgres."""

'''Подключение к базе данных'''
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='Stepa123')

'''Создание курсора для выполнения SQL-запросов'''
cur = conn.cursor()

'''Открыть CSV-файл с данными'''
try:
    with open('north_data\customers_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        ''' Прочитать и вставить данные в таблицу'''
        for row in reader:
            cur.execute('INSERT INTO customers ("customer_id", "company_name", "contact_name") VALUES (%s, %s, %s)', row)
        conn.commit()

    with open('north_data\employees_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        'Прочитать и вставить данные в таблицу'
        for row1 in reader:
            cur.execute('INSERT INTO employees (employee_id, "first_name", "last_name", "title", "birth_date", "notes") VALUES (%s, %s, %s, %s, %s, %s)', row1)
        conn.commit()

    with open('north_data\orders_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row2 in reader:
            cur.execute('INSERT INTO orders (order_id, "customer_id", employee_id, "order_date", "ship_city") VALUES (%s, %s, %s, %s, %s)', row2)
        conn.commit()

finally:
    conn.close()


if __name__ == "__main__":
    main()



