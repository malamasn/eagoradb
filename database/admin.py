from django.contrib import admin
from .models import *

admin.site.site_header = 'E Agora DB'

admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Supplier)
admin.site.register(Selling)
admin.site.register(Orders)
admin.site.register(Has)
