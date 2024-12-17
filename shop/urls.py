from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.shop_all, name='shop-all'),
    path('sellers/', views.sellers, name='shop-sellers'),
    path('sellers/<int:id>_<str:name>/', views.seller, name='seller-inventory'),
    path('clothing/', views.clothing_category, name='clothing_category'),
    path('beauty/', views.beauty_category, name='beauty_category'),
    path('jewelry/', views.jewelry_category, name='jewelry_category'),
    path('shoes/', views.shoes_category, name='shoes_category'),
    path('search/', views.search, name='shop-search'),
    path('<int:id>/<slug:name>/', views.view_product, name='product-view'),
    path('sort/', views.sort, name='sort'),
    path('<int:id>/<slug:name>/review', views.add_review, name='add_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
