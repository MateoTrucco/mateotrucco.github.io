from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/<str:job_date>/', views.jobs_by_date, name='jobs_by_date'),
    path('all_jobs/', views.all_jobs, name='all_jobs'),
    path('upload/', views.upload_job, name='upload_job'),
]
