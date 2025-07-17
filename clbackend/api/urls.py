from django.urls import path
from . import views

urlpatterns = [
    path("bookmarks/", views.BookMarkListCreate.as_view(), name="bookmark-list" ),
    path("bookmakrs/delete/<int:pk>", views.BookMarkDelete.as_view(), name="delete-bookmark"),
    path("bookmarks/update/<int:pk>", views.BookMarkUpdate.as_view(), name="update-bookmark"),
    path("cars/", views.CarListCreate.as_view(), name="car-list-create"),
    path("cars/<int:pk>/", views.CarPaymentDetail.as_view(), name="car-paylist"),
    path("corporate/<str:corporate_number>/", views.get_corporate_info, name="corporate-info"),
]