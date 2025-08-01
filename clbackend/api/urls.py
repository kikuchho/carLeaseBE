from django.urls import path
from . import views

urlpatterns = [
    path("bookmarks/", views.BookMarkListCreate.as_view(), name="bookmark-list" ),
    path("bookmarks/<int:pk>/", views.BookMarkDetail.as_view(), name="bookmark-detail"),
    path("bookmarks/delete/<int:pk>/", views.BookMarkDelete.as_view(), name="delete-bookmark"),
    path("bookmarks/update/<int:pk>/", views.BookMarkUpdate.as_view(), name="update-bookmark"),
    path("cars/", views.CarListCreate.as_view(), name="car-list-create"),
    path("cars/<int:pk>/", views.CarPaymentDetail.as_view(), name="car-paylist"),
    path("corporate/<str:corporate_number>/", views.get_corporate_info, name="corporate-info"),


    # Additional paths for car options page 
    path("cars/<int:pk>/options/", views.CarOptionsDetail.as_view(), name="car-options"),

    path("grades/", views.GradeListCreate.as_view(), name="grade-list-create"),
    path("grades/update/<int:pk>/", views.GradeUpdate.as_view(), name="grade-update"),
    path("colors/", views.ColorListCreate.as_view(), name="color-list-create"),
    path("colors/update/<int:pk>/", views.ColorUpdate.as_view(), name="color-update"),
    path("interiors/", views.InteriorListCreate.as_view(), name="interior-list-create"),
    path("optionpackages/", views.OptionPackageListCreate.as_view(), name="optionpackage-list-create"),
    path("optionpackages/update/<int:pk>/", views.OptionPackageUpdate.as_view(), name="optionpackage-update"),
    path("interiorexteriorupgrades/", views.InteriorExteriorUpgradeListCreate.as_view(), name="interiorexteriorupgrade-list-create"),
    path("interiorexteriorupgrades/update/<int:pk>/", views.InteriorExteriorUpgradeUpdate.as_view(), name="interiorexteriorupgrade-update"),
    path("tireupgrades/", views.TireUpgradeListCreate.as_view(), name="tireupgrade-list-create"),
    path("numberplates/", views.NumberplateListCreate.as_view(), name="numberplate-list-create"),
    path("numberplates/update/<int:pk>/", views.NumberplateUpdate.as_view(), name="numberplate-update"),

]