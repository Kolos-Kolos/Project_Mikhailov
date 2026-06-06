# ПЗ №17
# Вариант 16
# Форма регистрации на мастер-класс

from tkinter import *


def submit():
    print("Регистрация выполнена")
    print("Имя:", name_entry.get())
    print("Фамилия:", surname_entry.get())
    print("Email:", email_entry.get())
    print("Телефон:", phone_entry.get())


window = Tk()
window.title("Workshop Registration")
window.geometry("500x400")

# Заголовок
title_label = Label(
    window,
    text="Workshop Registration",
    font=("Arial", 16)
)
title_label.pack(pady=10)

# Имя
Label(window, text="First Name").pack()
name_entry = Entry(window, width=40)
name_entry.pack()

# Фамилия
Label(window, text="Last Name").pack()
surname_entry = Entry(window, width=40)
surname_entry.pack()

# Email
Label(window, text="Email").pack()
email_entry = Entry(window, width=40)
email_entry.pack()

# Телефон
Label(window, text="Phone").pack()
phone_entry = Entry(window, width=40)
phone_entry.pack()

# Пол
Label(window, text="Gender").pack()

gender = StringVar()
gender.set("Male")

Radiobutton(
    window,
    text="Male",
    variable=gender,
    value="Male"
).pack()

Radiobutton(
    window,
    text="Female",
    variable=gender,
    value="Female"
).pack()

# Кнопка регистрации
Button(
    window,
    text="Register",
    command=submit
).pack(pady=15)

window.mainloop()
```
