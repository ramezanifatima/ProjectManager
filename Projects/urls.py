from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectDeleteView, UpdateProjectView, ProjectDetailView, \
    TaskListView, DeleteTask, UpdateTask, AllTaskListView, TaskCreateView, TaskAndSubTaskListView, SubTaskView, \
    DeleteSubTask, UpdateSubTask, SubTaskCreateView,SubtaskDetailView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create/project', ProjectCreateView.as_view(), name='project_create'),
    path('delete/project/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('update/project/<int:pk>/', UpdateProjectView.as_view(), name='project_update'),
    path('detail/project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('list/task/', TaskListView.as_view(), name='task_list'),
    path('delete/task/<int:pk>', DeleteTask.as_view(), name='task_delete'),
    path('update/task/<int:pk>', UpdateTask.as_view(), name='task_update'),
    path('all/task/<int:id>', AllTaskListView.as_view(), name='task_all'),
    path('create/task/<int:id>', TaskCreateView.as_view(), name='task_create'),
    path('detaile/task/<int:id>', TaskAndSubTaskListView.as_view(), name='task_detail'),
    path('list/subtask/', SubTaskView.as_view(), name='subtask_list'),
    path('delete/subtask/<int:pk>', DeleteSubTask.as_view(), name='subtask_delete'),
    path('update/subtask/<int:pk>', UpdateSubTask.as_view(), name='subtask_update'),
    path('create/subtask/<int:id>', SubTaskCreateView.as_view(), name='subtask_create'),
    path('detail/subtask/<int:pk>', SubtaskDetailView.as_view(), name='subtask_detail'),
]
