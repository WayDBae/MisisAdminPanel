from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    created_at = models.DateTimeField(
        null=True, auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        null=True, auto_now=True, verbose_name="Дата обновления"
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата удаления"
    )

    class Meta:
        abstract = True  # Это делает класс абстрактным и он не будет создавать таблицу

    def soft_delete(self):
        """Мягкое удаление: устанавливает дату удаления."""
        self.deleted_at = now()
        self.save()

    def restore(self):
        """Восстановление объекта после мягкого удаления."""
        self.deleted_at = None
        self.save()

    @property
    def is_deleted(self):
        """Проверяет, является ли объект удаленным."""
        return self.deleted_at is not None


class Role(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название роли", null=False)

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        db_table = "roles"
        ordering = ["name"]

    def __str__(self):
        return self.name


class User(BaseModel):
    id = models.AutoField(primary_key=True)
    chat_id = models.TextField(
        verbose_name="Айди телеграма пользователя", null=False, unique=True
    )
    role = models.ForeignKey(
        Role, verbose_name="Роль пользователя", on_delete=models.CASCADE, null=True
    )
    phone_number = models.TextField(
        verbose_name="Номер телефона пользователя", null=True
    )
    username = models.TextField(verbose_name="Юзернейм пользователя", null=True)
    email = models.TextField(verbose_name="Имейл пользователя", null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "users"
        ordering = ["username"]

    def __str__(self):
        return self.username or self.chat_id


class Subject(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название предмета", null=False)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        db_table = "subjects"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ClassroomType(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Тип аудитории", null=False)

    class Meta:
        verbose_name = "Тип аудитории"
        verbose_name_plural = "Типы аудиторий"
        db_table = "classroom_types"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Classroom(BaseModel):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(
        ClassroomType, on_delete=models.CASCADE, related_name="classrooms"
    )
    description = models.TextField(verbose_name="Описание аудитории", null=True)
    floor = models.IntegerField(verbose_name="Этаж аудитории", null=False)
    capacity = models.IntegerField(verbose_name="Вместимость аудитории", null=True)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"
        db_table = "classrooms"
        ordering = ["floor", "type_id"]

    def __str__(self):
        return f"{self.type.name} (Этаж {self.floor})"


class Course(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название курса", null=False)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        db_table = "courses"
        ordering = ["name"]

    def __str__(self):
        return self.name


class GroupType(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Тип группы", null=False)

    class Meta:
        verbose_name = "Тип группы"
        verbose_name_plural = "Типы групп"
        db_table = "group_types"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Direction(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Тип направления", null=False)

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        db_table = "directions"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Education(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название обучения", null=False)

    class Meta:
        verbose_name = "Обучение"
        verbose_name_plural = "Обучения"
        db_table = "educations"
        ordering = ["name"]

    def __str__(self):
        return self.name


class EducationDirection(BaseModel):
    id = models.AutoField(primary_key=True)
    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, related_name="education_directions"
    )
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name="education_directions"
    )
    is_available_online = models.BooleanField(
        verbose_name="Доступно онлайн", null=False
    )

    class Meta:
        verbose_name = "Направление обучения"
        verbose_name_plural = "Направления обучений"
        db_table = "education_directions"

    def __str__(self):
        return f"{self.education.name} - {self.direction.name}"


class Group(BaseModel):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")
    type = models.ForeignKey(GroupType, on_delete=models.CASCADE, related_name="groups")
    education_direction = models.ForeignKey(
        EducationDirection, on_delete=models.CASCADE, related_name="groups"
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        db_table = "groups"

    def __str__(self):
        return f"{self.education_direction.direction.name} {self.education_direction.education.name} {self.course.name} ({self.type.name})"


class Event(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    short_name = models.TextField(null=False)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        db_table = "events"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Schedule(BaseModel):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="schedules")
    subject_detail = models.ForeignKey(
        "SubjectDetail", on_delete=models.CASCADE, related_name="schedules"
    )
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="schedules"
    )
    week_type = models.IntegerField(
        null=True, choices=[(1, "Числитель"), (2, "Знаменатель")]
    )
    date = models.DateField(null=True)
    day_of_week = models.IntegerField(
        null=True,
        choices=[
            (i, day)
            for i, day in enumerate(
                [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ],
                1,
            )
        ],
    )
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        db_table = "schedules"

    def __str__(self):
        return f"{self.group.course} {self.group.type} {self.group.education_direction.education} {self.group.education_direction.direction} - {self.subject_detail.teacher_subject.teacher.name} - {self.subject_detail.teacher_subject.subject.name} - {self.classroom} - {self.start_time} - {self.end_time}"


class Student(BaseModel):
    id = models.AutoField(primary_key=True)
    chat_id = models.TextField(
        verbose_name="Айди телеграма студента", null=False, unique=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, related_name="students"
    )
    name = models.TextField(verbose_name="Имя студента", null=False)
    surname = models.TextField(verbose_name="Фамилия студента", null=True)
    patronymic = models.TextField(verbose_name="Отчество студента", null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        db_table = "students"

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Teacher(BaseModel):
    id = models.AutoField(primary_key=True)
    chat_id = models.TextField(
        verbose_name="Айди телеграма преподавателя", null=False, unique=True
    )
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    patronymic = models.TextField(null=True)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        db_table = "teachers"

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class TeacherSubject(BaseModel):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="teacher_subjects"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="teacher_subjects"
    )

    class Meta:
        verbose_name = "Предмет преподавателя"
        verbose_name_plural = "Предметы преподавателей"
        db_table = "teacher_subjects"

    def __str__(self):
        return f"{self.teacher} - {self.subject}"


class SubjectDetail(BaseModel):
    id = models.AutoField(primary_key=True)
    teacher_subject = models.ForeignKey(
        TeacherSubject, on_delete=models.CASCADE, related_name="subject_details"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="subject_details"
    )

    class Meta:
        verbose_name = "Детали предмета"
        verbose_name_plural = "Детали предметов"
        db_table = "subject_details"

    def __str__(self):
        return f"{self.teacher_subject} ({self.event})"
