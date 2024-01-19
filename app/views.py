from django.shortcuts import render, HttpResponse, redirect
import razorpay
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import trial, client ,festival,package,search,payments
from django.contrib import messages

# Create your views here.



def home(request):
    fest= festival.objects.all()
    # se= festival.objects.all()
    # context = {'fest':fest}
    if request.method=='POST':
        name = request.POST.get('city-to')
        result = search.objects.filter(destination=name)
        # link = result.link
        return render(request, 'home.html',{'fest':fest,'result':result})
    
    return render(request, 'home.html',{'fest':fest})

def nikhil(request):
    trials = trial.objects.get(id=1)
    trial_amount = trials.trial_input_2
    trial_amount_2 = trial_amount * 100
    client = razorpay.Client(auth=('rzp_test_ClH6E4FgEWpPoz', 'UbdU2Jdi241y6fNAZKA7Bi1Q'))
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        print(razorpay_payment_id)
        payment = client.payment.fetch(razorpay_payment_id)
        payment_amount = int(payment['amount'])
        print(payment_amount)
        order = client.order.create({'amount': payment_amount, 'currency': 'INR', 'payment_capture': '1'})
        razorpay_order_id = request.POST.get('razorpay_order_id')
        print(razorpay_order_id)
        # return redirect(home)

    return render(request, 'nikhil.html', {'trial_amount': trial_amount_2})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()
        messages.succes(request,"Your Travel X account has been created successfully")
   

    return render(request, '.html')

def goa(request):
    return render(request, 'goa.html')
def prem(request):
    return render(request, 'prem.html')
def sun_temple(request):
    return render(request, 'sun_temple.html')
def varanasi(request):
    return render(request, 'varanasi.html')
def Dwarka(request):
    return render(request, 'Dwarka.html')

def success(request):
    return render(request, 'success.html')

def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = client.objects.all()

    return render(request, "list_view.html", context)

def user(request):
    if request.method =="POST":
        # print("username")
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        ins = client(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        ins.save()
        print(username)
        # return redirect(home)

    return render(request,'index.html')

def payment(request):
    if request.method =="POST":
        title=request.POST['label_6']
        first_name=request.POST['sublabel_6_first']
        last_name=request.POST['sublabel_6_last']
        budget=request.POST['label_7']
        email=request.POST['label_7']
        phone=request.POST['label_7']
        address=request.POST['password']
        month=request.POST['password']
        day=request.POST['password']
        year=request.POST['password']
        departing_from=request.POST['password']
        destination=request.POST['password']
        no_people=request.POST['password']

        pay = payments(title=title,first_name=first_name,last_name=last_name,budget=budget,email=email,phone=phone,address=address,month=month,day=day,year=year,departing_from=departing_from,destination=destination,no_people=no_people)
        pay.save()

    return render(request,'success.html')

def package(request):
    if request.method =="POST":
        city=request.POST['city']
        name=request.POST['name']
        sub_title=request.POST['sub_title']
        img=request.POST['img']
        price=request.POST['price']
        sub_price=request.POST['sub_price']
        discount=request.POST['discount']
        duration=request.POST['duration']
        day1=request.POST['day1']
        day2=request.POST['day2']
        day3=request.POST['day3']
        day4=request.POST['day4']
        place1=request.POST['place1']
        place2=request.POST['place2']
        place3=request.POST['place3']
        place4=request.POST['place4']
        hotel1=request.POST['hotel1']
        hotel2=request.POST['hotel2']
        hotel3=request.POST['hotel3']
        hotel4=request.POST['hotel4']
        pack = package(city=city,name=name,sub_title=sub_title,img=img,price=price,sub_price=sub_price,discount=discount,duration=duration,day1=day1,day2=day2,day3=day3,day4=day4,place1=place1,place2=place2,place3=place3,place4=place4,hotel1=hotel1,hotel2=hotel2,hotel3=hotel3,hotel4=hotel4)
        pack.save()
        return redirect(package)

    return render(request,'.html')

# def search(request):
#    travel = search.objects.all()
#    context = {'travel':travel}
#    return render(request,search.html)