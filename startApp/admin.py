from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from startApp.models import Customer, Course, Lesson, Enrollment, Test, Question, Category, Answer

admin.site.register(Customer)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
