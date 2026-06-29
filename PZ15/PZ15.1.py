import sqlite3


def create_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        issue_date TEXT NOT NULL,
        deadline TEXT NOT NULL,
        executor TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    print("\nДобавление поручения")

    title = input("Название поручения: ")
    issue_date = input("Дата выдачи: ")
    deadline = input("Срок исполнения: ")
    executor = input("Исполнитель: ")

    cursor.execute("""
    INSERT INTO tasks(title, issue_date, deadline, executor)
    VALUES (?, ?, ?, ?)
    """, (title, issue_date, deadline, executor))

    conn.commit()
    conn.close()

    print("Поручение добавлено.")


def show_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("База данных пуста.")
    else:
        print("\nСписок поручений:")
        for row in rows:
            print(row)

    conn.close()


def search_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    print("""
Поиск:
1 - по номеру
2 - по названию
3 - по исполнителю
""")

    choice = input("Выберите: ")

    if choice == "1":
        value = input("Введите номер: ")
        cursor.execute("SELECT * FROM tasks WHERE id=?", (value,))

    elif choice == "2":
        value = input("Введите название: ")
        cursor.execute("SELECT * FROM tasks WHERE title=?", (value,))

    elif choice == "3":
        value = input("Введите исполнителя: ")
        cursor.execute("SELECT * FROM tasks WHERE executor=?", (value,))

    else:
        print("Ошибка выбора.")
        conn.close()
        return

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("Ничего не найдено.")

    conn.close()


def delete_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    print("""
Удаление:
1 - по номеру
2 - по названию
3 - по исполнителю
""")

    choice = input("Выберите: ")

    if choice == "1":
        value = input("Введите номер: ")
        cursor.execute("DELETE FROM tasks WHERE id=?", (value,))

    elif choice == "2":
        value = input("Введите название: ")
        cursor.execute("DELETE FROM tasks WHERE title=?", (value,))

    elif choice == "3":
        value = input("Введите исполнителя: ")
        cursor.execute("DELETE FROM tasks WHERE executor=?", (value,))

    else:
        print("Ошибка выбора.")
        conn.close()
        return

    conn.commit()

    print("Удаление выполнено.")

    conn.close()


def edit_task():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    print("""
Редактирование:
1 - по номеру
2 - по названию
3 - по исполнителю
""")

    choice = input("Выберите: ")

    new_title = input("Новое название: ")
    new_issue = input("Новая дата выдачи: ")
    new_deadline = input("Новый срок: ")
    new_executor = input("Новый исполнитель: ")

    if choice == "1":
        value = input("Введите номер: ")

        cursor.execute("""
        UPDATE tasks
        SET title=?, issue_date=?, deadline=?, executor=?
        WHERE id=?
        """, (new_title, new_issue, new_deadline, new_executor, value))

    elif choice == "2":
        value = input("Введите название для поиска: ")

        cursor.execute("""
        UPDATE tasks
        SET title=?, issue_date=?, deadline=?, executor=?
        WHERE title=?
        """, (new_title, new_issue, new_deadline, new_executor, value))

    elif choice == "3":
        value = input("Введите исполнителя: ")

        cursor.execute("""
        UPDATE tasks
        SET title=?, issue_date=?, deadline=?, executor=?
        WHERE executor=?
        """, (new_title, new_issue, new_deadline, new_executor, value))

    else:
        print("Ошибка выбора.")
        conn.close()
        return

    conn.commit()

    print("Данные изменены.")

    conn.close()


def main():
    create_db()

    while True:
        print("""
========= МЕНЮ =========
1. Добавить поручение
2. Показать все поручения
3. Найти поручение
4. Удалить поручение
5. Редактировать поручение
6. Выход
========================
""")

        choice = input("Выберите пункт: ")

        try:
            if choice == "1":
                add_task()

            elif choice == "2":
                show_tasks()

            elif choice == "3":
                search_task()

            elif choice == "4":
                delete_task()

            elif choice == "5":
                edit_task()

            elif choice == "6":
                print("Работа завершена.")
                break

            else:
                print("Неверный пункт меню.")

        except Exception as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
