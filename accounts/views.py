from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    from_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


