from django.urls import path
from .views import PersonList, PersonUpdate

urlpatterns = [
    path('', PersonList.as_view(), name='person_read'),
    path('update/<int:pk>', PersonUpdate.as_view(), name='person_update'),
]
