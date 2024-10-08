from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Project
from .forms import ProjectForm, UpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class ProjectListView(LoginRequiredMixin, ListView):
    """
    this view will return all of the projects
    """
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user=request.user)
        context = {
            'projects': projects
        }
        return render(request, 'Projects/projects.html', context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """
    this view
    """
    form_class = ProjectForm
    template_name = 'Projects/create_project.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            data = form.cleaned_data
            project = Project.objects.create(
                user=user,
                title=data['title'], image=data['image'],
                description=data['description'], color=data['color'],
                start_date=data['start_date'], end_date=data['end_date'],
                budget=data['budget']
            )
            if project:
                messages.success(request, 'your project saved')
                return redirect('projects:projects_list')
            messages.error(request, 'something went wrong', 'danger')
        else:
            form = self.form_class(instance=user)
            return render(request, 'Projects/create_project.html', {'form': form})


class ProjectDeleteView(DeleteView):
    """

    """
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'Projects/delete_project.html'
    success_url = '/'


class UpdateProjectUpdate(UpdateView):
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'Projects/delete_project.html'
    success_url = '/'


class UpdateProjectView(UpdateView):
    """

    """
    model = Project
    form_class = UpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'Projects/update.html'
    success_url = '/'
