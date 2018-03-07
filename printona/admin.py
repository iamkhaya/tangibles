from django.contrib import admin

from .models import Order
from .models import OrderItem
from .models import Product
from .models import User

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(User)
