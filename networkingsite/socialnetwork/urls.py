from rest_framework import routers
from django.urls import path
from .views import LoginViewSet, SignUpViewSet, UserViewSet

router = routers.DefaultRouter()
app_name = "socialnetwork"

router.register(r"sign-up", SignUpViewSet, basename="sign-up")
router.register(r"search-user", UserViewSet, basename="search-user")

urlpatterns = [
    path("login/", LoginViewSet.as_view(), name="login")
] + router.urls

