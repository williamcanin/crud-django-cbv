from django.urls import path
from .views import PersonList, PersonUpdate, PersonCreate

urlpatterns = [
    path('', PersonList.as_view(), name='person_read'),
    path('update/<int:pk>', PersonUpdate.as_view(), name='person_update'),
    path('new/', PersonCreate.as_view(), name='person_new'),
]
