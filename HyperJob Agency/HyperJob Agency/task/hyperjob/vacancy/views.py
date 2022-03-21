from django.shortcuts import render, redirect
from .models import Vacancy
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied


def layout(request):
    return render(request, "resume/layout.html", context={'user': request.user})

def get_vacancy(request):
    return render(request, 'vacancy/vacancylist.html', context={'vacancies': Vacancy})

def vacancy_new(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()

    if not request.user.is_staff:
        raise PermissionDenied()

    return render(request, "vacancy/vacancy_new.html", context={'user': request.user})

def vacancy_save(request):
    newvacancy = Vacancy.objects.create(author=request.user, description=request.POST["description"])
    newvacancy.save()
    return layout(request)

def vacancylist(request):
    return render(request, 'vacancy/vacancylist.html', context={'vacancies': Vacancy})


class VacanciesListView(ListView):
    model = Vacancy

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacanciesListView, self).get_context_data(**kwargs)
        return context
