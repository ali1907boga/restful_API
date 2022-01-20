from django.urls import path
from .views import *

urlpatterns = [

    path('api/comments/',CommentList.as_view()),
    path('api/comments/<int:pk>/like',SendLike.as_view()),
    path('api/comments/<int:pk>/delete/',CommentRetrieveDestroy.as_view()),


]