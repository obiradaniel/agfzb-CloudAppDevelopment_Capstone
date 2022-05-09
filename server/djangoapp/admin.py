from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.
#admin.site.register(CarMake)
#admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'dealer_id', 'car_type', 'year']
    list_filter = ['car_type', 'year']
    search_fields = ['name', 'dealer_id', 'car_type', 'year']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'description', 'manufacturer' ]
    list_filter = ['name', 'description', 'manufacturer' ]
    search_fields = ['name', 'description', 'manufacturer' ]

# Register models here

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
