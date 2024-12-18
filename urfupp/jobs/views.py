from django.shortcuts import render, redirect
from .models import Jobs
from .forms import JobsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import JobSearchForm
from django.contrib.auth.decorators import permission_required


def jobs_home(request):
    jobs = Jobs.objects.order_by('-date')
    return render(request, 'jobs/index.html', {'jobs': jobs})

class JobsDetailView(DetailView):
    model = Jobs
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

class JobsUpdateView(UpdateView):
    model = Jobs
    template_name = 'jobs/create.html'

    form_class = JobsForm

class JobsDeleteView(DeleteView):
    model = Jobs
    success_url = '/jobs'
    template_name = 'jobs/job_delete.html'

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

def search_jobs(request):
    form = JobSearchForm(request.GET or None)
    jobs = Jobs.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('query')
        type_of_job = form.cleaned_data.get('type_of_job')
        if query:
            jobs = jobs.filter(title__icontains=query) | jobs.filter(desc__icontains=query)
        if type_of_job:
            if isinstance(type_of_job, str):
                jobs = jobs.filter(type_of_job=type_of_job)
            else:
                jobs = jobs.filter(type_of_job=type_of_job)

    return render(request, 'jobs/search.html', {'form': form, 'jobs': jobs})

def add_job(request):
    pass

def profile(request):
    pass