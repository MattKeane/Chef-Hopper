from django.urls import path

from . import views

urlpatterns = [
	path("test_route/", views.test_route, name='test route'),
]