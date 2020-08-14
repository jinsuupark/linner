from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .form import CreateUserForm

# 순수하게 html 템플릿만 운영할 수 있도록 도와주는
# 공통 사용할 것~~~~~~~~~~~~~~~~~

class HomeView(TemplateView):
    template_name = 'home.html'
class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('signup_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/signup_done.html'