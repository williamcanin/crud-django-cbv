from django.urls import path
from .views import ClientList, ClientUpdate, ClientCreate, ClientDetails, ClientDelete


urlpatterns = [
    path("", ClientList.as_view(), name="client_read"),
    path("update/<int:pk>", ClientUpdate.as_view(), name="client_update"),
    path("new/", ClientCreate.as_view(), name="client_new"),
    path("details/<int:pk>", ClientDetails.as_view(), name="client_details"),
    path("delete/<int:pk>", ClientDelete.as_view(), name="client_delete"),
]
