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
        ''' Прочитать и вставить данные в таблицу'''
        for row in reader:
            customer_id, company_name, contact_name = row
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', (customer_id, company_name, contact_name))

    with open('north_data\employees_data.csv', 'r') as file:
        reader = csv.reader(file)
        'Прочитать и вставить данные в таблицу'
        for row1 in reader:
            employee_id, first_name, last_name, title, birth_date, notes = row1
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)', (employee_id, first_name, last_name, title, birth_date, notes))

    with open('north_data\orders_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row2 in reader:
            order_id, customer_id, employee_id, order_date, ship_city = row2
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)', (order_id, customer_id, employee_id, order_date, ship_city))

finally:
    conn.close()


if __name__ == "__main__":
    main()



