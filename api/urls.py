from django.urls import path

from . import views

urlpatterns = [
	path("test_route/", views.test_route, name='test route'),
	path("recipes/search/<query>", views.search, name="get recipes"),
	path("auth/register/", views.register, name="register user")
]