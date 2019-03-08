from django.contrib import admin

from .models import Categories
admin.site.register(Categories)

from .models import SubCategories
admin.site.register(SubCategories)

from .models import Product
admin.site.register(Product)


from .models import Manufacturer
admin.site.register(Manufacturer)


from .models import Customer
admin.site.register(Customer)


from .models import Invoice
admin.site.register(Invoice)



