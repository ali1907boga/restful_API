from django.urls import path
from . import views

app_name = 'api_again'
urlpatterns = [

    path('all_api/',views.All_Api.as_view()),
    path('article/<int:pk>/',views.Article_Detail.as_view()),
    path('users/',views.UserList.as_view()),
    path('user/<int:pk>/',views.User_Detail.as_view(),name='user_detail'),


]