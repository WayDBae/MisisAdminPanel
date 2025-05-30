# Generated by Django 5.1.4 on 2024-12-29 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Тип аудитории')),
            ],
            options={
                'verbose_name': 'Тип аудитории',
                'verbose_name_plural': 'Типы аудиторий',
                'db_table': 'classroom_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'db_table': 'courses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Тип направления')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
                'db_table': 'directions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название обучения')),
            ],
            options={
                'verbose_name': 'Обучение',
                'verbose_name_plural': 'Обучения',
                'db_table': 'educations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'db_table': 'events',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GroupType',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Тип группы')),
            ],
            options={
                'verbose_name': 'Тип группы',
                'verbose_name_plural': 'Типы групп',
                'db_table': 'group_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название роли')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
                'db_table': 'roles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'db_table': 'subjects',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_id', models.TextField(unique=True, verbose_name='Айди телеграма преподавателя')),
                ('name', models.TextField(null=True)),
                ('surname', models.TextField(null=True)),
                ('patronymic', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(null=True, verbose_name='Описание аудитории')),
                ('floor', models.IntegerField(verbose_name='Этаж аудитории')),
                ('capacity', models.IntegerField(null=True, verbose_name='Вместимость аудитории')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to='bot.classroomtype')),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
                'db_table': 'classrooms',
                'ordering': ['floor', 'type_id'],
            },
        ),
        migrations.CreateModel(
            name='EducationDirection',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_available_online', models.BooleanField(verbose_name='Доступно онлайн')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_directions', to='bot.direction')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_directions', to='bot.education')),
            ],
            options={
                'verbose_name': 'Направление обучения',
                'verbose_name_plural': 'Направления обучений',
                'db_table': 'education_directions',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='bot.course')),
                ('education_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='bot.educationdirection')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='bot.grouptype')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_id', models.TextField(unique=True, verbose_name='Айди телеграма студента')),
                ('name', models.TextField(verbose_name='Имя студента')),
                ('surname', models.TextField(null=True, verbose_name='Фамилия студента')),
                ('patronymic', models.TextField(null=True, verbose_name='Отчество студента')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='bot.group')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='SubjectDetail',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_details', to='bot.event')),
            ],
            options={
                'verbose_name': 'Детали предмета',
                'verbose_name_plural': 'Детали предметов',
                'db_table': 'subject_details',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('week_type', models.IntegerField(choices=[(1, 'Числитель'), (2, 'Знаменатель')], null=True)),
                ('date', models.DateField(null=True)),
                ('day_of_week', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.TextField(null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bot.classroom')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bot.group')),
                ('subject_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='bot.subjectdetail')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
                'db_table': 'schedules',
            },
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subjects', to='bot.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_subjects', to='bot.teacher')),
            ],
            options={
                'verbose_name': 'Предмет преподавателя',
                'verbose_name_plural': 'Предметы преподавателей',
                'db_table': 'teacher_subjects',
            },
        ),
        migrations.AddField(
            model_name='subjectdetail',
            name='teacher_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_details', to='bot.teachersubject'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_id', models.TextField(unique=True, verbose_name='Айди телеграма пользователя')),
                ('phone_number', models.TextField(null=True, verbose_name='Номер телефона пользователя')),
                ('username', models.TextField(null=True, verbose_name='Юзернейм пользователя')),
                ('email', models.TextField(null=True, verbose_name='Имейл пользователя')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.role', verbose_name='Роль пользователя')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
                'ordering': ['username'],
            },
        ),
    ]
