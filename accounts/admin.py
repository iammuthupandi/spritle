from django.contrib import admin
from .models import User,Master,Student,Calculation

admin.site.register(User)
admin.site.register(Master)
admin.site.register(Student)
admin.site.register(Calculation)