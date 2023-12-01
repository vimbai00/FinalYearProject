from django.contrib import admin
from .models import Staff,Paddock,Department,Livestock,TimeLine,Sales,Debtors

# Register your models here.
admin.site.register([Staff,Paddock,Department,Livestock,TimeLine,Sales,Debtors  ])
