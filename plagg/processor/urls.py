from django.urls import path
from processor import views

urlpatterns = [
    path("", view=views.index, name="name"),
    path("post_file/", view=views.post_file, name="post_file")
]
