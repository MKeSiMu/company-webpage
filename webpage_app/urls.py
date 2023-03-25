from django.urls import path

from webpage_app.views import index

urlpatterns = [
    path("", index, name="index"),
    ]

app_name = "webpage_app"
