
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^sum', views.number_sum),

]