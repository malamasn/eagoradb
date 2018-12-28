from django.urls import path
from django.contrib.auth.views import login, logout

from . import views

app_name = 'database'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', login, {'template_name': 'database/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'database/logout.html'}, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='view_profile'),
    path('password/', views.PasswordView.as_view(), name='change_password'),

    path('', views.HomeView.as_view(), name = 'home'),
    path('find_products/', views.FindProducts.as_view(), name = 'find_products'),
    path('find_stores/', views.FindStores.as_view(), name = 'find_stores'),
    path('product_<int:pk>/', views.ProductView.as_view(), name = 'product'),
    path('store_<int:pk>/', views.StoreView.as_view(), name = 'store'),


]
