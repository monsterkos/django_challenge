from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
	path("create/<int:obj>", views.create_review, name="create"),
	path("delete/<int:obj>", views.delete_review, name="delete")
]