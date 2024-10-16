from django.contrib import admin
from django.urls import path
from startApp import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('home_page/', views.home_page, name='home_page'),
    path('course/<int:course_id>/', views.course_detail, name='course-detail'),
    path('category/<int:category_id>/', views.category_detail, name='category-detail'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson-detail'),
    path('test/<int:test_id>/', views.test_detail, name='test-detail'),
    path('profile/', views.profile, name='profile'),
    path('create_course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('about_project/', views.about_project, name='about_project'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

