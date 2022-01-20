from django.urls import path
from . import views

app_name= 'api'
urlpatterns = [

    path('api/',views.ArticleList.as_view(),name = 'list'),
    path('api/<int:pk>/',views.ArticleDetail.as_view(),name = 'detail'),
    path('users/',views.UserList.as_view(),name = 'users'),


]
