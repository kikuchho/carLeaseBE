from django.urls import path
from . import views

urlpatterns = [
    path("bookmarks/", views.BookMarkListCreate.as_view(), name="bookmark-list" ),
    path("bookmakrs/delete/<int:pk>", views.BookMarkDelete.as_view(), name="delete-bookmark"),
    path("bookmarks/update/<int:pk>", views.BookMarkUpdate.as_view(), name="update-bookmark")
]