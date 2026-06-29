# Приложение КОНТРОЛЬ ИСПОЛНЕНИЯ ПОРУЧЕНИЙ для некоторой
#организации. БД должна содержать таблицу Поручения со следующей структурой записи:
#Порядковый номер поручения, Название поручения, Дата выдачи поручения, Срок
#исполнения, Исполнитель

import sqlite3

try:
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT,
            issue_date TEXT,
            deadline TEXT,
            employee TEXT
        )
    """)

    # Очистка таблицы
    cursor.execute("DELETE FROM tasks")

    # Добавление 10 записей
    tasks = [
        (1, "Отчет", "01.03.2025", "05.03.2025", "Иванов"),
        (2, "Смета", "02.03.2025", "06.03.2025", "Петров"),
        (3, "Договор", "03.03.2025", "10.03.2025", "Сидоров"),
        (4, "Проверка", "04.03.2025", "08.03.2025", "Иванов"),
        (5, "Закупка", "05.03.2025", "12.03.2025", "Смирнов"),
        (6, "Анализ", "06.03.2025", "13.03.2025", "Петров"),
        (7, "Инвентаризация", "07.03.2025", "15.03.2025", "Кузнецов"),
        (8, "План", "08.03.2025", "16.03.2025", "Сидоров"),
        (9, "Контроль", "09.03.2025", "18.03.2025", "Иванов"),
        (10, "Отчет по проекту", "10.03.2025", "20.03.2025", "Петров")
    ]

    cursor.executemany(
        "INSERT INTO tasks VALUES (?, ?, ?, ?, ?)",
        tasks
    )

    conn.commit()

    print("=== ПОИСК ===")

    # Поиск №1
    cursor.execute(
        "SELECT * FROM tasks WHERE employee='Иванов'"
    )
    print(cursor.fetchall())

    # Поиск №2
    cursor.execute(
        "SELECT * FROM tasks WHERE id=5"
    )
    print(cursor.fetchall())

    # Поиск №3
    cursor.execute(
        "SELECT * FROM tasks WHERE title='Анализ'"
    )
    print(cursor.fetchall())

    print("\n=== УДАЛЕНИЕ ===")

    # Удаление №1
    cursor.execute(
        "DELETE FROM tasks WHERE id=10"
    )

    # Удаление №2
    cursor.execute(
        "DELETE FROM tasks WHERE employee='Кузнецов'"
    )

    # Удаление №3
    cursor.execute(
        "DELETE FROM tasks WHERE title='Закупка'"
    )

    conn.commit()

    print("Удаление выполнено")

    print("\n=== РЕДАКТИРОВАНИЕ ===")

    # Редактирование №1
    cursor.execute("""
        UPDATE tasks
        SET employee='Орлов'
        WHERE id=1
    """)

    # Редактирование №2
    cursor.execute("""
        UPDATE tasks
        SET deadline='25.03.2025'
        WHERE title='План'
    """)

    # Редактирование №3
    cursor.execute("""
        UPDATE tasks
        SET title='Финансовый отчет'
        WHERE id=2
    """)

    conn.commit()

    print("Редактирование выполнено")

    print("\n=== ВСЕ ЗАПИСИ ===")

    cursor.execute("SELECT * FROM tasks")

    for row in cursor.fetchall():
        print(row)

    conn.close()

except sqlite3.Error as error:
    print("Ошибка базы данных:", error)

except Exception as error:
    print("Ошибка:", error)
