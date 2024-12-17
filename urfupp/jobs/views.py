from django.shortcuts import render, redirect
from .models import Jobs
from .forms import JobsForm
from django.views.generic import DetailView

def jobs_home(request):
    jobs = Jobs.objects.order_by('-date')
    return render(request, 'jobs/index.html', {'jobs': jobs})

class JobsDetailView(DetailView):
    model = Jobs
    temp_name = 'jobs/job_detail.html'
    context_object_name = 'job'

def create(request):
    error = ''
    if request.method == 'POST':
        form = JobsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('jobs-home')
        else:
            error = 'неверно заполнена форма'

    form = JobsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'jobs/create.html', data)
