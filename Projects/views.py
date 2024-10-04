from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy


class ProjectListView(LoginRequiredMixin,ListView):
    """
    this view will return all of the projects
    """
    login_url = reverse_lazy('accounts:user_login')

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        context = {
            'projects': projects
        }
        return render(request, 'Projects/list_projects.html', context)
