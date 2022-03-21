from importlib._common import _
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Resume
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .userforms import UserUpdateForm


def update_profile(request):
    if not request.user.is_authenticated:
        return base_layout(request)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, _('Ваш профиль был успешно обновлен!'))
            return redirect('/')
        else:
            messages.error(request, _('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserUpdateForm(instance=request.user)

    return render(request, 'resume/profile.html', {
        'user_form': user_form,
        'user_authentificate': request.user.is_authenticated,
        'user': request.user
    })


def signup(request):
    return UserCreationForm.default_renderer()


def base_layout(request):
    return render(request, "resume/layout.html", context={'user': request.user})


def layout(request):
    return update_profile(request)


def resumelist(request):
    return render(request, 'resume/resumelist.html')


def resume_save(request):
    newresume = Resume.objects.create(author=request.user, description=request.POST["description"])
    newresume.save()
    return resumelist(request)


def resume_new(request):
    if request.POST:
        return resume_save(request)

    return render(request, "resume/resume_new.html", context={'user': request.user})


class ResumesListView(ListView):
    model = Resume

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResumesListView, self).get_context_data(**kwargs)

        return context


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'resume/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'resume/login.html'


class MyLogOutView(LogoutView):
    next_page = '/home'
