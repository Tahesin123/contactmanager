from .views import *
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("index/",user_index),
    path("show-contacts/",show_contact),
    path("add-contact/",add_contact),
    path("delete-contact/<int:id>",delete_contact),
    path("update-contact/<int:id>",update_contact),
    path("updated-contact/<int:id>",updated_contact),
]

