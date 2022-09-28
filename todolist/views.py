from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm

# Create your views here.
from todolist.models import todolistItem #Kalau masih abu abu segera buat modulnya!

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    userdata=todolistItem.objects.filter(user=request.user)
    context = {
    'user_data' : userdata,
    }
    return render(request, "todolist.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


    
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login')
def createtask(request):
     form = TaskForm()

     if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            todo=   form.save(commit=False)
            todo.user=request.user
            todo.save()
            form.save_m2m()
            return redirect('todolist:show_todolist')
     context = {"forms": form,}

     return render(request, 'createtask.html', context)
    
@login_required(login_url='/todolist/login/')
def deletetask(request,id):
    hapus=todolistItem.objects.get(pk=id)
    if hapus:
        hapus.delete()
        return redirect('todolist:show_todolist')
    

@login_required(login_url='/todolist/login/')
def finishedtask(request,id):
    finish=todolistItem.objects.get(pk=id)
    if finish:
        finish.is_finished=False if finish.is_finished else True
        finish.save()
        return redirect('todolist:show_todolist')
    
