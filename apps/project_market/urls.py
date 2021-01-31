from django.urls import path

from . import views

app_name = 'project_market'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project, name='project'),
    path('new_project/', views.new_project, name="new_project"),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('review_project/<int:project_id>', views.review_project, name='review_project'),
]