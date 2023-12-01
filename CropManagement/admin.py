from django.contrib import admin
from .models import Staff,Field,Farm,Crops,TimeLine,Sales,Debtors

# Register your models here.
admin.site.register([Staff,Field,Farm,Crops,TimeLine,Sales,Debtors  ])