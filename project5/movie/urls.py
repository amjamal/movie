from django.urls import path
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:update_id>/', views.update, name='update'),
    path('delete/<int:delete_id>/', views.delete, name='delete')
]
