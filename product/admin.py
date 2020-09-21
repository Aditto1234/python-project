from django.contrib import admin
from .models import Category, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description')


admin.site.register(Category,CategoryAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','description','cat')


admin.site.register(Image,ImageAdmin)

# Register your models here.
