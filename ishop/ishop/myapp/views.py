from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, UpdateView, CreateView
# from django.views.generic.edit import FormView, UpdateView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from .models import Tovar, Purchase, Vozvrat, MyUser
from .forms import MyForm, CreateTovarForm, UpdateTovarForm, CreatePurchaseForm
from django.shortcuts import render


def home(request):
    return render(request, template_name="home.html")


class RegisterFormView(FormView):
    # form_class = UserCreationForm
    form_class = MyForm
    success_url = "/login/"
    template_name = "login/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


"""Если для регистрации достаточно только логина и пароля, файл forms.py не нужно создавать, 
в классе class RegisterFormView(FormView) заменить form_class = UserCreationForm,
и соответственно не импортировать MyForm, но обязательно from django.contrib.auth.forms import UserCreationForm"""


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = "login/login.html"


class LogoutFormView(LogoutView):
    next_page = "/"


class CreateTovar(CreateView):
    model = Tovar
    form_class = CreateTovarForm
    success_url = '/create/'
    template_name = 'tovar/tovar_add.html'


class TovarUpdateView(UpdateView):
    template_name = 'tovar/tovar_update.html'
    form_class = UpdateTovarForm
    success_url = '/see/'
    model = Tovar


class TovarListView(ListView):
    model = Tovar
    paginate_by = 5
    template_name = 'tovar/tovar_see.html'
    # success_url = '/see/'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context.update(
            {'tovar_create_form': CreateTovarForm,
             'tovar_update_form': UpdateTovarForm}
        )
        return context


class CreatePurchase(CreateView):
    model = Purchase
    form_class = CreatePurchaseForm
    success_url = '/see/'
    template_name = 'tovar/tovar_buy.html'
