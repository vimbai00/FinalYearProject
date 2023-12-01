from django.contrib import admin
from .models import Staff,Dam,Department,Fish,TimeLine,Sales,Debtors

# Register your models here.
admin.site.register([Staff,Dam,Department,Fish,TimeLine,Sales,Debtors  ])