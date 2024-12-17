from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobs_home, name='jobs-home'),
    path('create', views.create, name='create-job'),
    path('<int:pk>', views.JobsDetailView.as_view(), name='jobs-detail')
]