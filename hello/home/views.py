from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import create_user, authenticate_user
import pandas as pd
from home.models import CustomUser
# Create your views here.
def index(request):
    return HttpResponse(render(request, template_name="signup.html"))

def home(request):
    return HttpResponse(render(request, template_name="index.html"))

#for check the table 
def table(request):
    query_results = CustomUser.objects.all()
    data=list(query_results.values())
    df=pd.DataFrame(data)
    print(df)
    return HttpResponse('tabel entered successfully in tarminal ')

# for delete the row from table
def quary(request):
    row_to_delete = CustomUser.objects.get(id=4)
    row_to_delete.delete()
    return HttpResponse('successfully deleted')

#signup backend 
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Basic validation to ensure password matches
        if password != password2:
            return HttpResponse("password not match")
        else:
            
            create_user(name, email, phone, password)
            return redirect('login')
            

    return render(request, template_name="signup.html")

#login backend
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate_user(email, password)
        
        if user is not None:
            
            return redirect('index')
        else:
            return HttpResponse("wrong email or password")

    return render(request, template_name="login.html")
