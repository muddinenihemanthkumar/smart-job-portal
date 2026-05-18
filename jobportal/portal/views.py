from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):

    search = request.GET.get('search')

    if search:
        jobs = Job.objects.filter(
            title__icontains=search
        )
    else:
        jobs = Job.objects.all()

    return render(
        request,
        'home.html',
        {'jobs': jobs}
    )

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'success.html', {'job': job})
def job_detail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_detail.html', {'job': job})

from django.shortcuts import render, redirect
from .models import Job

def add_job(request):
    if request.method == "POST":
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        salary = request.POST['salary']
        description = request.POST['description']

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            description=description
        )

        return redirect('/')

    return render(request, 'add_job.html')

def edit_job(request, id):
    job = Job.objects.get(id=id)

    if request.method == "POST":
        job.title = request.POST['title']
        job.company = request.POST['company']
        job.location = request.POST['location']
        job.salary = request.POST['salary']
        job.description = request.POST['description']

        job.save()

        return redirect('/')

    return render(request, 'edit_job.html', {'job': job})

def delete_job(request, id):
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/')