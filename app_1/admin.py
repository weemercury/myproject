from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone_number', 'registration_date']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Введите имя.'
    list_per_page = 5
    
    readonly_fields = ['registration_date']
    
    fieldsets = [
        ('Personal INFO',
            {'fields': ['name'],
            'description': 'Info about client.',
            'classes': ['wide'],
            }
        ),
        ('More INFO',
            {'fields': ['address', 'registration_date'],
             'description': 'More Info about client.',
             'classes': ['collapse'],
             }
        ),
        ('Contacts',
            {'fields': ['email', 'phone_number'],
             'description': 'Contacts of client.',
             'classes': ['wide'],
             }
         )
    ]
    

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity_of_products', 'add_date']
    list_filter = ['add_date']
    list_editable = ['quantity_of_products']
    ordering = ['price']
    search_fields = ['name']
    search_help_text = 'Введите название товара.'
    list_per_page = 5
    
    fieldsets = [
        ('INFO',
            {'fields': ['name'],
            'description': 'Name of product.',
            'classes': ['wide'],
            }
        ),
        ('Description',
            {'fields': ['description'],
             'description': 'Description of product.',
             'classes': ['collapse'],
             }
        ),
        ('More INFO',
            {'fields': ['price', 'quantity_of_products', 'add_date'],
             'description': 'More INFO about product.',
             'classes': ['wide'],
             }
         )
    ]
    

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['clients', 'total_price', 'date_ordered']
    list_filter = ['date_ordered']
    ordering = ['-total_price']
    search_fields = ['clients']
    search_help_text = 'Введите имя клиента.'
    list_per_page = 7
    
    
    fieldsets =[
        ('INFO', {
            'fields': ['clients', 'products', 'total_price', 'date_ordered'],
            'classes': ['collapse'],
            }
        ),
    ]
