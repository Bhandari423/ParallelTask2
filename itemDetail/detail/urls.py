from django.urls import path
from . import views

urlpatterns = [
    path("create-item/", views.CreateDetail.as_view()),
    path("show-item/", views.CreateDetail.as_view()),
    path("delete-item/<int:pk>", views.CreateDetail.as_view()),
]