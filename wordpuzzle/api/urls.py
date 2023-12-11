from django.contrib import admin
from django.urls import path

from .views import WordPuzzleApi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wordpuzzle", WordPuzzleApi.as_view(), name="wordpuzzle"),
]
