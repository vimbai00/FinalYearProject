from django.contrib import admin
from .models import Staff,Flock,Department,Chicken,TimeLine,Sales,Debtors

# Register your models here.
admin.site.register([Staff,Flock,Department,Chicken,TimeLine,Sales,Debtors  ])
