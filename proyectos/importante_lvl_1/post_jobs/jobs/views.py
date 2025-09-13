from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import date, timedelta

def home(request):
    today = date.today()
    last_three_days = [today - timedelta(days=i) for i in range(6)]
    jobs = {day: Job.objects.filter(date_posted=day) for day in last_three_days}
    return render(request, 'jobs/home.html', {'jobs': jobs, 'last_three_days': last_three_days})

def jobs_by_date(request, job_date):
    jobs = Job.objects.filter(date_posted=job_date)
    return render(request, 'jobs/jobs_by_date.html', {'jobs': jobs, 'job_date': job_date})

def all_jobs(request):
    jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs/all_jobs.html', {'jobs': jobs})

def upload_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirigir a la página principal u otra después de subir el trabajo
    else:
        form = JobForm()
    
    return render(request, 'jobs/upload_job.html', {'form': form})