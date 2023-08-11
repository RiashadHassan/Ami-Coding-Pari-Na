from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import InputItemForm
from django.contrib.auth import authenticate, login, logout
from django.views import View

def home(request):
    
    context={}
    return render(request, 'base/home.html', context)

#i can work with both function based views as well as class based views

#SECTION 1

def register_user(request):
    
    form =UserCreationForm() 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request, new_user)
            return HttpResponse('logged in')
    context = {'form':form}
    return render(request, 'base/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')

class LoginPageView(View):
    template_name= 'base/login.html'
    
    def get(self, request):        
        context={}
        return render(request, self.template_name, context)
    
    def post(self, request):
        username= request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else: 
            return HttpResponse('could not log in')
        
        
#SECTION 2

class Search(View):
    template_name = 'base/search.html'
    
    def get(self, request):
        form = InputItemForm()
        context= {'form': form}
        return render (request, self.template_name, context)
    
    def post(self, request):
        form= InputItemForm(request.POST)
        if form.is_valid():
            input_numbers = form.cleaned_data['input_numbers']
            
            try:
                input_numbers_list= [int(number.strip()) for number in input_numbers.split(',')]
            except:
                return HttpResponse("Please enter valid integer values separated by commas.")
                           
            
            sorted_input_numbers_list = sorted(input_numbers_list, reverse=True)
            
            input_instance= form.save(commit=False)
            input_instance.user = request.user
            input_instance.input_numbers=','.join(map(str, sorted_input_numbers_list))
            input_instance.save()
            
            result = form.check_search_input(sorted_input_numbers_list)
            context = {'form': form, 'result':result}
            return render (request, self.template_name, context)
        else: 
            return HttpResponse('invalid form')