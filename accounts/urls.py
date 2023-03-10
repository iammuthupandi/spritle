from . import views
from django.urls import path


urlpatterns = [
    path('',views.register,name='register'),
    path('master_register/', views.master_register.as_view(), name='master_register'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('master_login/', views.master_login, name='master_login'),
    path('student_login/', views.student_login, name='student_login'),
    path('master_home/', views.master_home, name='master_home'),
    path('student_home/', views.student_home, name='student_home'),
]