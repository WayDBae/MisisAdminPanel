# bot/admin.py
from django.contrib import admin
from django import forms
from .models import (
    Teacher,
    Subject,
    Classroom,
    Schedule,
    ClassroomType,
    Course,
    Direction,
    Education,
    EducationDirection,
    Event,
    Group,
    GroupType,
    Role,
    Student,
    SubjectDetail,
    TeacherSubject,
    User
)

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    # Настроим виджеты для полей (например, для текстовых полей)
    chat_id = forms.TextInput(attrs={'size': '30'})  # Уменьшаем размер поля
    name = forms.TextInput(attrs={'size': '30'})
    surname = forms.TextInput(attrs={'size': '30'})
    patronymic = forms.TextInput(attrs={'size': '30'})

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ('surname', 'name', 'patronymic', 'chat_id')
    fields = ('chat_id', 'surname', 'name', 'patronymic')

    # Можете использовать inline формы, чтобы сделать админку ещё компактнее


admin.site.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'surname', 'group', 'chat_id')
#     search_fields = ['name', 'surname', 'chat_id']
#     list_filter = ('group',)


admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(ClassroomType)
admin.site.register(Course)
admin.site.register(Direction)
admin.site.register(Education)
admin.site.register(EducationDirection)
admin.site.register(Event)
admin.site.register(Group)
admin.site.register(GroupType)
admin.site.register(Role)
admin.site.register(SubjectDetail)
admin.site.register(TeacherSubject)
admin.site.register(User)
