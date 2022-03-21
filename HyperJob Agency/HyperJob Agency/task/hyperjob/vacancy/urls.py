from django.urls import path, re_path
from .views import VacanciesListView, vacancy_new, layout
from .models import Vacancy


vacancies_list_view = VacanciesListView.as_view(
    queryset=Vacancy.objects.order_by('author'),
    context_object_name="vacancy_list",
    template_name="vacancy/vacancylist.html",

)

urlpatterns = [
    re_path("new", vacancy_new, name="vacancy_new"),
    re_path("ies", vacancies_list_view, name="vacancylist"),
    # path("", layout, name="layout"),
]
