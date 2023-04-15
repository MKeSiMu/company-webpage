from django.urls import path

from webpage_app.views import (
    index,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerPublicCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    ManufacturerDetailView,
    BearingTypeListView,
    BearingTypeDetailView, BearingTypeCreateView, BearingTypeUpdateView, BearingTypeDeleteView
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
        "manufacturer-form/",
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
    ),
    path(
        "bearing-types/",
        BearingTypeListView.as_view(),
        name="bearing-type-list",
    ),
    path(
        "bearing-types/<int:pk>/",
        BearingTypeDetailView.as_view(),
        name="bearing-type-detail",
    ),
    path(
        "bearing-types/create/",
        BearingTypeCreateView.as_view(),
        name="bearing-type-create",
    ),
    path(
        "bearing-types/<int:pk>/update/",
        BearingTypeUpdateView.as_view(),
        name="bearing-type-update",
    ),
    path(
        "bearing-types/<int:pk>/delete/",
        BearingTypeDeleteView.as_view(),
        name="bearing-type-delete",
    ),
    ]

app_name = "webpage_app"
