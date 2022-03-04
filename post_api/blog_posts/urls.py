from django.urls import path
from . import views


urlpatterns = [
    path("api/post/", views.PostApiView.as_view(), name="post-view"),
]
