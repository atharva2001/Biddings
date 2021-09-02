from django.shortcuts import redirect, render
from datetime import datetime, time, timedelta, date
from Bidwars.models import Register
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    try:
        if request.method == "POST":
            request.session['name'] = request.POST.get('name')
            request.session['email'] = request.POST.get('email')
            request.session['password'] = request.POST.get('password')
            request.session['plan'] = request.GET.get('plan')


            if request.session['plan'] == "Basic":
                date = datetime.today() + timedelta(days=25)
            elif request.session['plan'] == "Pro":
                date = datetime.today() + timedelta(days=45)
            else:
                date = datetime.today() + timedelta(days=365)

            reg = Register.objects.filter(email=request.session['email']).exists()
            if reg != True:
                registers = Register(name=request.session['name'], email=request.session['email'],
                                            password=request.session['password'],plan=request.session['plan'], date=date)
                registers.save()
                messages.error(request, "Registered!")
                return redirect('/login')
            else:
                messages.error(request, "Email Exists!")
                return redirect('/register') 
    except Exception as e:
        messages.error(request, "Something went wrong!")
        return redirect('/login')
        
    return render(request, 'register.html')
