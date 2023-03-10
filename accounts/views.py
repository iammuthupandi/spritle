from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import MasterSignUpForm, StudentSignUpForm
from .models import User,Calculation
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.shortcuts import render
from .calculator import *

def register(request):
    return render(request,'register.html')

@login_required(login_url='register')
def master_home(request):
        context = {}
        if request.method == "POST":
            expression = request.POST.get('expression')
            result = eval(expression)
            context['result'] = result

            calculation = Calculation.objects.create(expression=expression,result=result)
            calculation.save()
        return render(request, 'master_home.html', context)


@login_required(login_url='register')
def student_home(request):
    result = Calculation.objects.all()
    return render(request,'student_home.html',context={'result':result})


class master_register(CreateView):
    model = User
    form_class = MasterSignUpForm
    template_name = 'master_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/master_home/')

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/student_home/')

def master_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/master_home/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'master_login.html',context={'form':AuthenticationForm()})


def student_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/student_home/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'student_login.html',context={'form':AuthenticationForm()})
