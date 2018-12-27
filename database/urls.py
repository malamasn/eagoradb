from django.urls import path

from . import views

app_name = 'database'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.HomeView.as_view(), name = 'home'),
    path('find_products/', views.FindProducts.as_view(), name = 'find_products'),
    path('find_stores/', views.FindStores.as_view(), name = 'find_stores'),
    path('product_<int:pk>/', views.ProductView.as_view(), name = 'product'),
    path('store_<int:pk>/', views.StoreView.as_view(), name = 'store'),


]
