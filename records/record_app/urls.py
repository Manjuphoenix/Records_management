from django.urls import path, include

from .views import *

app_name = 'record_app'
urlpatterns = [
    path("", listAuthorRecords, name="index"),
    path("search", SearchView.as_view(), name="search_results"),
    path('author/', listAuthorRecords, name="index"),
    path("keyword", listKeywordsRecords, name="index1"),
    path("title", listTitleRecords, name="index2"),
    path("about", about, name="about"),
]


