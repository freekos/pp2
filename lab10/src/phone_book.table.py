from psycopg2 import Error
import csv

from config import load_config
from database_connect import connect

def create_table():
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()
        
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS phoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()
        
    except Error as e:
        print("Ошибка при создании таблицы:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def add_contact(name, phone):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()
        
        insert_query = '''
        INSERT INTO phoneBook (name, phone)
        VALUES (%s, %s)
        '''
        cursor.execute(insert_query, (name, phone))
        connection.commit()
        
    except Error as e:
        print("Ошибка при добавлении контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_contact(contact_id, new_name, new_phone):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        update_query = '''
        UPDATE phoneBook 
        SET name = %s, phone = %s 
        WHERE id = %s
        '''
        cursor.execute(update_query, (new_name, new_phone, contact_id))
        connection.commit()
    except Error as e:
        print("Ошибка при обновлении данных контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def get_all_contacts():
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()
        
        select_query = '''
        SELECT * FROM phoneBook
        '''
        cursor.execute(select_query)
        contacts = cursor.fetchall()
        
        for contact in contacts:
            print(contact)
        
    except Error as e:
        print("Ошибка при получении контактов:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def load_data_from_csv(csv_file):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        with open(csv_file, 'r', newline='') as file:
            print(file)
            reader = csv.DictReader(file)

            insert_query = '''
            INSERT INTO phoneBook (name, phone) VALUES (%s, %s)
            '''

            for row in reader:
                cursor.execute(insert_query, (row['name'], row['phone']))

            connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто.")

def delete_contact(contact_id):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        delete_query = '''
        DELETE FROM phoneBook 
        WHERE id = %s
        '''
        cursor.execute(delete_query, (contact_id,))
        connection.commit()

        print("Контакт успешно удален.")

    except Error as e:
        print("Ошибка при удалении контакта:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()

def search_contacts(filter_name):
    try:
        config = load_config()
        connection = connect(config)
        cursor = connection.cursor()

        search_query = '''
        SELECT * FROM phoneBook 
        WHERE name LIKE %s
        '''
        cursor.execute(search_query, ('%' + filter_name + '%',))
        contacts = cursor.fetchall()
        
        return contacts
    except Error as e:
        print("Ошибка при поиске контактов:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    res = input("Выберите тип измененей:\n1. Консоль\n2. CSV файл\nВведите: ")

    if res == '1':
        res = input("Выберите команду консоли:\n1. Добавить контакт\n2. Обновить контакт\n3. Удалить контакт\n4. Искать контакты по имени: \n")
        if res == '1':
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            add_contact(name, phone)
            get_all_contacts()
        elif res == '2':
            id = input("Введите имя айди пользователя: ")
            name = input("Введите новое имя контакта: ")
            phone = input("Введите новый номер телефона: ")
            update_contact(id, name, phone)
            get_all_contacts()
        elif res == '3':
            name = input("Введите имя контакта: ")
            contacts = search_contacts(name)
            delete_contact(contacts[0][0])
            get_all_contacts()
        elif res == '4':
            name = input("Введите имя контакта: ")
            print(search_contacts(name))
    elif res == '2':
        csv_file = input("Введите путь к CSV файлу: ")
        load_data_from_csv(csv_file, "phoneBook")
        get_all_contacts()
