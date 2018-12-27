from django.urls import path

from . import views

app_name = 'database'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name = 'home'),
    path('find_products/', views.FindProducts.as_view(), name = 'find_products'),
    path('find_stores/', views.FindStores.as_view(), name = 'find_stores'),

]
