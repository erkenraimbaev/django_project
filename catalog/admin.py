from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category',)
    list_filter = ()
    search_fields = ('name_category', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_product', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name_product', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'name_version', 'product', 'current_version')
    list_filter = ('product',)
    search_fields = ('name_version', 'current_version',)
