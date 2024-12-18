from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_home, name='jobs-home'),
    path('create', views.create, name='create-job'),
    path('<int:pk>', views.JobsDetailView.as_view(), name='job-detail'),
    path('<int:pk>/update', views.JobsUpdateView.as_view(), name='job-update'),
    path('<int:pk>/delete', views.JobsDeleteView.as_view(), name='job-delete'),
    path('<int:pk>/apply', views.apply_for_job, name='job-apply'),
    path('search', views.search_jobs, name='search'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:pk>', views.delete_application, name='job-apply-delete'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]