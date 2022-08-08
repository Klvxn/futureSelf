from django.contrib.auth.views import LoginView as Login, logout_then_login
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User

from .forms import SignupForm


# Create your views here.
class SignupView(FormView):

    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('letter:my_letters')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        user = User.objects.create(username=username, email=email, password=password)
        login(self.request, user)
        return super().form_valid(form)


class LoginView(Login):

    template_name = 'login.html'
    
    def get(self, request,  *args, **kwargs):
        logout_then_login(self.request)
        return super().get(request, *args, **kwargs)