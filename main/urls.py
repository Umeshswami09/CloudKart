from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login_page, name='login'),

    path('logout/', views.logout_page, name='logout'),

    path('products/', views.products, name='products'),

    path('categories/', views.categories, name='categories'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    # Live Search
    path('search/', views.search_products, name='search_products'),

    # Product Detail
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]