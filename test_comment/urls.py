from django.urls import path
from . import views

urlpatterns = [

    path('all_comment/',views.All_Comment.as_view()),
    path('all_comment2/',views.Posst.as_view()),
    path('delete/<int:pk>/',views.DeleteUpdateGet.as_view()),
    path('send_like/<int:pk>/',views.SendLike.as_view()),
    path('sendlike/<int:pk>/',views.Sendlike.as_view()),

]