from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'post_content', 'image', 'date_of_create', 'publication_sign', 'count_of_views')
    list_filter = ()
    search_fields = ('slug', 'post_content',)
