from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    path('', views.index, name='home'),
    path('movie/<int:pk>/', views.details, name="moviedetail"),
    path('add/', views.add_movies, name="addmovies"),
    path('edit/<int:pk>/', views.update, name="updatedetails"),
    path('delete/<int:pk>/', views.delete, name="deletefilm"),
]
