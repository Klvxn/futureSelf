from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import LoginView, SignupView


# Urls
app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sign-up/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]



