from telebot import types


def StartInlineKeyboard(buttons: list[str]) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for button_text in buttons:
        keyboard.add(
            types.InlineKeyboardButton(text=button_text, callback_data=button_text)
        )
    return keyboard


def StatusInlineKeyboard():
    status_key = types.InlineKeyboardMarkup(row_width=2)
    student_btn = types.InlineKeyboardButton(
        text="👨‍🎓Студент", callback_data="👨‍🎓Студент"
    )
    teacher_btn = types.InlineKeyboardButton(
        text="👨‍🏫Преподаватель", callback_data="👨‍🏫Преподаватель"
    )
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="menu")
    status_key.add(student_btn, teacher_btn, back_btn)
    return status_key


def LearningKeyboard():
    learning_key = types.InlineKeyboardMarkup(row_width=2)
    fullTime = types.InlineKeyboardButton(text="Очное", callback_data="Очное")
    campus = types.InlineKeyboardButton(text="ДЗО", callback_data="ДЗО")
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="user_type")
    learning_key.add(fullTime, campus, back_btn)
    return learning_key


def CourseKeyboard():
    course_key = types.InlineKeyboardMarkup(row_width=2)
    buttons = ["1", "2", "3", "4"]
    for button in buttons:
        course_key.add(
            types.InlineKeyboardButton(
                text=f"{button} курс", callback_data=f"{button} курс"
            )
        )
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    course_key.add(back_btn)
    return course_key


def GroupKeyboard(direction, course):
    group_key = types.InlineKeyboardMarkup(row_width=2)
    back_btn = types.InlineKeyboardButton("Назад", callback_data="Назад")

    if direction == 1 and course in [1, 2, 3]:
        group_a_btn = types.InlineKeyboardButton("Группа А", callback_data="А")
        group_b_btn = types.InlineKeyboardButton("Группа Б", callback_data="Б")
        group_key.add(group_a_btn, group_b_btn, back_btn)
    elif direction == 3 and course in [1, 2]:
        group_a_btn = types.InlineKeyboardButton("Группа А", callback_data="А")
        group_b_btn = types.InlineKeyboardButton("Группа Б", callback_data="Б")
        group_key.add(group_a_btn, group_b_btn, back_btn)
    else:
        group_a_btn = types.InlineKeyboardButton("Группа А", callback_data="А")
        group_key.add(group_a_btn, back_btn)

    return group_key


def WeekKeyboard():
    week = types.InlineKeyboardMarkup(row_width=5)
    today_btn = types.InlineKeyboardButton(text="Сегодня", callback_data="Сегодня")
    week.add(today_btn)
    monday_btn = types.InlineKeyboardButton("Пн", callback_data="Понедельник")
    tuesday_btn = types.InlineKeyboardButton("Вт", callback_data="Вторник")
    wednesday_btn = types.InlineKeyboardButton("Ср", callback_data="Среда")
    thursday_btn = types.InlineKeyboardButton("Чт", callback_data="Четверг")
    friday_btn = types.InlineKeyboardButton("Пт", callback_data="Пятница")
    week.add(monday_btn, tuesday_btn, wednesday_btn, thursday_btn, friday_btn)
    profile_btn = types.InlineKeyboardButton(text="Профиль", callback_data="Профиль")
    back_btn = types.InlineKeyboardButton("Назад", callback_data="Назад")
    week.add(profile_btn, back_btn)
    return week


def ErrorKeyboard():
    key = types.InlineKeyboardMarkup(row_width=1)
    error_btn = types.InlineKeyboardButton(
        text="Написать разработчику", url="https://t.me/waydbae"
    )
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    key.add(error_btn, back_btn)
    return key


def BackKeyboard():
    key = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
    key.add(back_btn)
    return key


def TeacherKeyboard():
    """
    Создает клавиатуру для выбора ФИО преподавателя.

    Возвращает:
    InlineKeyboardMarkup: Клавиатура с кнопками для выбора преподавателя.
    """
    # Создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    # Предполагаем, что у вас есть список преподавателей
    # Здесь должен быть ваш код для получения списка преподавателей из базы данных
    teachers_list = ["Иванов И.И.", "Петров П.П.", "Сидоров С.С."]

    # Добавляем кнопки для каждого преподавателя
    for teacher in teachers_list:
        teacher_btn = types.InlineKeyboardButton(
            text=teacher, callback_data=f"teacher_{teacher}"
        )
        keyboard.add(teacher_btn)

    # Добавляем кнопку "Назад"
    back_btn = types.InlineKeyboardButton(text="Назад", callback_data="user_type")
    keyboard.add(back_btn)

    return keyboard
