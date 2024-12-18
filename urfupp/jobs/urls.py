from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_home, name='jobs-home'),
    path('create', views.create, name='create-job'),
    path('<int:pk>', views.JobsDetailView.as_view(), name='job-detail'),
    path('<int:pk>/update', views.JobsUpdateView.as_view(), name='job-update'),
    path('<int:pk>/delete', views.JobsDeleteView.as_view(), name='job-delete'),
    path('search/', views.search_jobs, name='search'),
]