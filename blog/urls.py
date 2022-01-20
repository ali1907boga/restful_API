from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [

    path('',views.ArticlelIST.as_view(),name = 'home'),
    path('blog/<int:pk>/',views.ArticleDetail.as_view(),name = 'detail')

]