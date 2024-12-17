from django.shortcuts import render

def jobs_home(request):
    return render(request, 'jobs/index.html')
