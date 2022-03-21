from django.contrib import admin
from django.urls import path
from .views import layout, ResumesListView, MyLoginView, MySignUpView, resume_new, resume_save, update_profile, MyLogOutView
from .models import Resume
from django.contrib.auth.views import LogoutView

resume_list_view = ResumesListView.as_view(
    queryset=Resume.objects.order_by('author'),
    context_object_name='resume_list',
    template_name="resume/resumelist.html",
)

urlpatterns = [
    path("", layout, name="profile"),
    path("home", layout, name="profile"),
    path("resume/new", resume_new, name="resume_new"),
    path("resume/save", resume_save, name="resumelist"),
    path("resumes", resume_list_view, name="resumelist"),
    path('login', MyLoginView.as_view()),
    path('logout', MyLogOutView.as_view()),
    path('signup', MySignUpView.as_view()),
    path('profile', update_profile, name='profile'),
    path('admin/', admin.site.urls),
]
