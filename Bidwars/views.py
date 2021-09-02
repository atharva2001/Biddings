from django.shortcuts import redirect, render
from datetime import datetime, time, timedelta, date
from Bidwars.models import Register, Profile, Item, Store
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def profile(request):
    try:
       if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            item = Item.objects.filter(name=name,email=email)
            pro = Profile.objects.filter(name=name, email=email).exists()
            print(pro, item)
            if pro == True:
                pro = Profile.objects.get(name=name, email=email)
                reg = Register.objects.get(name=name,email=email,password=password)
                if reg.date >= date.today():
                    return render(request, 'profile.html',{'reg':reg, 'item':item, 'pro':pro})
                else:
                    messages.error(request, "Your free trial expired!")
                    return redirect('/register')
            else:
                pro = {
                    'address' : 'NA',
                    'phone' : 'NA',
                    'country' : 'NA',
                }
                reg = Register.objects.get(name=name,email=email,password=password)
                print(reg)
                if reg.date >= date.today():
                    return render(request, 'profile.html',{'reg':reg, 'item':item, 'pro':pro})
                else:
                    messages.error(request, "Your free trial expired!")
                    return redirect('/register')
                
    except Exception as e:
        print(e)
        messages.error(request, "Invalid Credentials")
        return redirect('/login')
        
    return render(request, 'profile.html')

def login(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")

            reg = Register.objects.get(name=name,email=email,password=password)
            return render(request, 'profile.html',{'reg':reg})
    except Exception as e:
        print(e)
        messages.error(request, "Invalid Credentials!")
        return redirect('/login')
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
