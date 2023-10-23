from django.urls import path,include
from . import views

urlpatterns = [   
    path('',views.home,name = "home"),
    path('movie/<movie_id>', views.homePage, name="homepage"),
    path('contact-us',views.contact, name="contact"),
    path('about-us',views.about,name="about"),
    path('search',views.Search, name="search"),
    path('category',views.category,name="categorylist"),
    path('category/<slug:category_slug>/', views.category, name="category"),

]
