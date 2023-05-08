from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("new_dashboard", views.new_dashboard, name="new_dashboard"),
    path("<int:dashboard_id>/delete", views.dashboard_delete, name="dashboard_delete"),
    path("<int:dashboard_id>/dashboard", views.dashboard_view, name="dashboard_view"),

    path("<int:dashboard_id>/point_create", views.point_create, name="point_create"),
    path("<int:point_id>/point_delete", views.point_delete, name="point_delete"),
]

