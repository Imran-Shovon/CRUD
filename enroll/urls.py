from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_show, name="add-show"),
    path('delete/<int:id>', views.delete_data, name="delete-data"),
    path('<int:id>', views.update_data, name="update-data"),
]
