# from django.urls import @app.get('/path_name')
# def method_name():
#     pass
from django.contrib import admin
from django.urls import path, include
from . import views

app_name="links"

urlpatterns = {
    path("create/", views.PostCreateApi.as_view(), name="api_create"),
    path("update/<int:pk>", views.PostUpdateApi.as_view(), name="api_update"),
    path("delete/<int:pk>", views.PostDeleteApi.as_view(), name="api_delete"),
    path("", views.PostListApi.as_view(), name = "api_list"),
    path("api/links/", include("links.urls")),
}