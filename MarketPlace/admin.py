from django.contrib import admin
from .models import Customer, Product, Orders, Feedback

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrdersAdmin(admin.ModelAdmin):  # Change OrderAdmin to OrdersAdmin
    pass
admin.site.register(Orders, OrdersAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
