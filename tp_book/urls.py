from django.urls import path
from tp_book.views import *
urlpatterns = [

    path('get-all-data/',GetAllData.as_view()),
    path('get-fav-data/',GetFavData.as_view()),
    path('update-fav-data/<int:pk>/',UpdateFvaData.as_view()),
    path('PostModel/',PostModel.as_view()),
    path('search/',SearchData.as_view()),
    path('delete_update_get/<int:pk>/',DeleteUpdateGet.as_view()),
    path('allapi/',allapi),
    path('postapi/',PostApi,),
    path('update_delete_get/<int:pk>/',update_delete_get),
    path('book/',BookList.as_view()),
    path('journalist/',JournalistList.as_view()),




]