from django.contrib import admin
from blog.models import Post, BlogComment, Category
# Register your models here.

admin.site.register((BlogComment,)) # it must be in tupple formate
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyInject.js",)
