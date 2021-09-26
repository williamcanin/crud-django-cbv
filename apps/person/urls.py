from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PersonList, PersonUpdate, PersonCreate, PersonDetails, PersonDelete

urlpatterns = [
    path('', PersonList.as_view(), name='person_read'),
    path('update/<int:pk>', PersonUpdate.as_view(), name='person_update'),
    path('new/', PersonCreate.as_view(), name='person_new'),
    path('details/<int:pk>', PersonDetails.as_view(), name='person_details'),
    path('delete/<int:pk>', PersonDelete.as_view(), name='person_delete'),
]
