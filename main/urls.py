from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('averave_info',views.aboutaverave),
    path('contacts',views.contacts)
]