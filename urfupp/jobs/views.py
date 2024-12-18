from django.shortcuts import render, redirect
from .models import Jobs
from .forms import JobsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import SearchForm
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


def search_view(request):
    query = request.GET.get('query', '')
    results = Jobs.objects.filter(title__icontains=query) if query else None
    form = SearchForm(initial={'query': query})
    return render(request, 'jobs/search.html', {'form': form, 'results': results})

def add_job(request):
    pass

def profile(request):
    pass