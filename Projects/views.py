from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project, Task, SubTask
from .forms import ProjectForm, UpdateProjectForm, TaskForm, TaskUpdateForm, SubTaskForm, SubTaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse


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
    This view is used to create a new project
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
    This view is used to delete a project
    """
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'Projects/delete_project.html'
    success_url = '/'


class UpdateProjectView(UpdateView):
    """
    This view is used to edit a project
    """
    model = Project
    pk_url_kwarg = 'pk'
    form_class = UpdateProjectForm
    template_name = 'Projects/update.html'
    success_url = '/'


class DetailProjectView(DetailView):
    """
    This view returns the details of a project
    """
    model = Project
    pk_url_kwarg = 'pk'
    template_name = 'Projects/mor_info_project.html'


class DetailTaskView(DetailView):
    """
    This view returns the details of a task and show mor subtasks
    """
    model = Task
    template_name = 'Projects/mor_info_task.html'


class CreateTaskView(CreateView):
    """

    """
    form_class = TaskForm
    template_name = 'Projects/create_task.html'
    pk_url_kwarg = 'pk_project'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        pk_project = self.kwargs.get(self.pk_url_kwarg)
        project = get_object_or_404(Project, pk=pk_project)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            task = Task.objects.create(
                project=project, title=data['title'],
                description=data['description'], color=data['color'],
                image=data['image'], start_date=data['start_date'],
                end_date=data['end_date'], budget=data['budget'],
            )
            if task:
                print('task')
                messages.success(request, 'your task saved ')
                return redirect(reverse('projects:projects_detail', kwargs={'pk': pk_project}))
            messages.error(request, 'something went wrong', 'danger')
        else:
            print(form.errors)
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = 'pk'
    template_name = 'Projects/delete_task.html'
    success_url = '/'


class UpdateTaskView(UpdateView):
    model = Task
    pk_url_kwarg = 'pk'
    form_class = TaskUpdateForm
    template_name = 'Projects/update_task.html'
    success_url = '/'


class CreateSubTaskView(CreateView):
    """

    """
    form_class = SubTaskForm
    template_name = 'Projects/create_sub_task.html'
    pk_url_kwarg = 'pk_task'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        pk_task = self.kwargs.get(self.pk_url_kwarg)
        task = get_object_or_404(Task, pk=pk_task)
        project = get_object_or_404(Project,task=task)

        if form.is_valid():
            data = form.cleaned_data
            task = SubTask.objects.create(
                task=task, title=data['title'],
                description=data['description'], color=data['color'],
                image=data['image'], start_date=data['start_date'],
                end_date=data['end_date'], budget=data['budget'],
            )
            if task:
                messages.success(request, 'your task saved ')
                return redirect(reverse('projects:projects_detail', kwargs={'pk': project.id}))
            messages.error(request, 'something went wrong', 'danger')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


class SubTaskDeleteView(DeleteView):
    model = SubTask
    pk_url_kwarg = 'pk'
    template_name = 'Projects/delete_subtask.html'
    success_url = '/'


class UpdateSubTaskView(UpdateView):
    model = SubTask
    pk_url_kwarg = 'pk'
    form_class = SubTaskUpdateForm
    template_name = 'Projects/update_subtask.html'
    success_url = '/'


class DetailSubTaskView(DetailView):
    """
    This view returns the details of a subtask
    """
    model = SubTask
    template_name = 'Projects/mor_info_task.html'
