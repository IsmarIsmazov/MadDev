from django.contrib import admin

from .models import Chair, Category, Material


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'discounted_price', 'width', 'height', 'depth', 'category', 'country',
                    'in_stock', 'pickup', 'delivery', 'created']
    list_filter = ['category', 'country', 'in_stock', 'pickup', 'delivery']
    search_fields = ['title', 'category__name', 'country']
    list_per_page = 20