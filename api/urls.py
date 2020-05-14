from django.urls import path

from . import views

urlpatterns = [
	path("test_route/", views.test_route, name='test route'),
	path("recipes/search/<query>", views.search, name="get recipes"),
	path("auth/register/", views.register, name="register user"),
	path("auth/logged_in_user/", views.get_logged_in_user, name="get logged in user"),
	path("auth/log_out/", views.log_out, name="log out user"),
	path("auth/log_in/", views.log_in, name="log in user")
]