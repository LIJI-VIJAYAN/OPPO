from django.contrib import admin
from app1.models import ProductDetails


# Register your models here.
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=('id','Name','Price','Description','Storagespace','Imagename')
admin.site.register(ProductDetails,ProductDetailsAdmin)
