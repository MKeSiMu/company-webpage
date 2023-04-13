from django.urls import path

from webpage_app.views import (
    index,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerPublicCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    ManufacturerDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail"
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/manufacturer-form/",
        ManufacturerPublicCreateView.as_view(),
        name="manufacturer-public-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    )
    ]

app_name = "webpage_app"
