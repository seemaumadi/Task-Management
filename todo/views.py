import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from .metrics import REQUESTS, CURRENT_TIME, update_metrics
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm
from .models import Task
from .metrics import track_http_requests, set_current_time




# Create your views here.
def metrics_view(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)
#function for home
def home(request):

    track_http_requests()  # Increment the request count
    set_current_time(time.time())  # Set the current time metric

    return render(request, 'index.html')

#function for register
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('my-login')
        
    context = {'form':form}

    return render(request, 'register.html', context=context)    

#function for login
    
def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        

    context = {'form':form}

    return render(request, 'my-login.html', context=context)    

@login_required(login_url="my-login")
def my_profile(request):

    pass


#function for dashboard
@login_required(login_url="my-login")
def dashboard(request):
    
    return render(request, 'profile/dashboard.html')


#function for profile-manage
@login_required(login_url="my-login")
def profile_manage(request):
    
    if request.method == "POST":

        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():

            user_form.save()

            return redirect('dashboard')
        
        
    user_form = UpdateUserForm(instance=request.user)

    context = {'user_form':user_form}  

    return render(request, 'profile/profile-manage.html', context=context)    

    

#function for create-task
@login_required(login_url="my-login")
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('view-tasks')
        
    context = {'form':form}

    return render(request, 'profile/create-task.html', context=context)


# function for view-task
@login_required(login_url="my-login")
def viewTask(request):
    
    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task':task}

    return render(request, 'profile/view-tasks.html', context=context)

#function for update-task
@login_required(login_url="my-login")
def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':

        form = CreateTaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('view-tasks')
        
    context = {'form':form}   
    
    return render(request, 'profile/update-task.html', context=context)

#function for delete-task
def deleteTask(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":

        task.delete()

        return redirect('view-tasks')
    
    return render(request, 'profile/delete-task.html')



#function for logout
def user_Logout(request):

    auth.logout(request)

    return redirect("")

def log_request_metrics(request):
    start_time = time.time()
    response = None
    try:
        response = request()
    finally:
        duration = time.time() - start_time
        update_metrics(request.method, request.path, duration)
    return response

# Middleware to log metrics for all requests
class MetricsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        update_metrics(request.method, request.path, duration)
        return response
