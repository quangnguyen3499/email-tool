from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/v1/contacts/",
        views.CreateContactAPIView.as_view(),
        name="save-mail-contact",
    ),
    path(
        "api/v1/contacts/list/",
        views.ListContactView.as_view(),
        name="list-mail-contact",
    ),
]
