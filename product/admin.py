from django.contrib import admin

from .models import Brand, Category, Product, Unit, StoreCatalog

admin.site.register(Brand)
admin.site.register(Unit)
admin.site.register(Category)

class StoreCatalogInline(admin.TabularInline):
    model = StoreCatalog

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        StoreCatalogInline,
    ]

admin.site.register(Product, ProductAdmin)
