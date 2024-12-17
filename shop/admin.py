from django.contrib import admin
from .models import Item, Reviews, Category, Supplier

# Item modeli için admin paneli yapılandırması
from django.contrib import admin


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('ItemID', 'ProductName', 'BrandName', 'Price', 'Size', 'Color', 'CategoryId')
    search_fields = ('ProductName', 'BrandName', 'Color')
    list_filter = ('BrandName', 'Color', 'Price')

# Reviews modeli için admin paneli yapılandırması
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('ReviewID', 'ItemID', 'SellerID', 'Ratings', 'Date')
    search_fields = ('ReviewID', 'ItemID', 'Ratings')
    list_filter = ('Ratings', 'Date')

# Category modeli için admin paneli yapılandırması
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('ID', 'Name', 'parent_id')
    search_fields = ('Name',)

# Supplier modeli için admin paneli yapılandırması
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('SellerID', 'FirstName', 'LastName', 'Email', 'CompanyName')
    search_fields = ('FirstName', 'LastName', 'CompanyName')
