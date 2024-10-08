from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDeleteView, UpdateProjectView, DetailProjectView, \
    DetailTaskView, CreateTaskView, TaskDeleteView, UpdateTaskView, DetailSubTaskView, SubTaskDeleteView, \
    CreateSubTaskView, UpdateSubTaskView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create', ProjectCreateView.as_view(), name='projects_create'),
    path('delete/project/<int:pk>', ProjectDeleteView.as_view(), name='projects_delete'),
    path('update/project/<int:pk>', UpdateProjectView.as_view(), name='projects_update'),
    path('project/<int:pk>', DetailProjectView.as_view(), name='projects_detail'),
    path('project/task/<int:pk>', DetailTaskView.as_view(), name='task_detail'),
    path('project/<int:pk_project>/create/task', CreateTaskView.as_view(), name='create_task'),
    path('delete/task/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('update/task/<int:pk>', UpdateTaskView.as_view(), name='task_update'),
    path('project/task/subtask/<int:pk>', DetailSubTaskView.as_view(), name='subtask_detail'),
    path('task/<int:pk_task>/create/subtask', CreateSubTaskView.as_view(), name='create_subtask'),
    path('delete/subtask/<int:pk>', SubTaskDeleteView.as_view(), name='subtask_delete'),
    path('update/subtask/<int:pk>', UpdateSubTaskView.as_view(), name='subtask_update'),

]
