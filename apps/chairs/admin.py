from django.contrib import admin

from .models import Chair, Category, Material

# Register your models here.
admin.site.register(Chair)
admin.site.register(Category)
admin.site.register(Material)
