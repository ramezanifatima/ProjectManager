from django.urls import path
from .views import ProjectListView,ProjectCreateView,UpdateProjectView

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create', ProjectCreateView.as_view(), name='projects_create'),
    path('delete/project/<int:pk>', ProjectCreateView.as_view(), name='projects_create'),
    path('update/project/<int:pk>', UpdateProjectView.as_view(), name='projects_update'),
]
