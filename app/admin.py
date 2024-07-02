from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Marca)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'marca', 'color', 'size', 'status')
    search_fields = ('title', 'slug')
    list_filter = ('marca', 'color', 'size')
    list_editable = ('status',)
    list_per_page = 10
admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)



