from django.shortcuts import render



from django.shortcuts import render,redirect 

from django.shortcuts import render, HttpResponseRedirect
from .forms import  SignUpForm, LoginForm

from .forms import ContactForm,Book_ground
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import Group


from django.core.mail import send_mail
from django.conf import settings

from .models import Contact,Book_ground







# Create your views here.

# home page navigation
def home_view(request):
 return render(request, 'C/home.html')


# footer page navigation
def footer_view(request):
 return render(request, 'C/footer.html')


# about page navigation
def about_view(request):
 return render(request, 'C/about.html')


# contact page detailes saved

def contact_view(request):
    if request.method == 'POST':
      fm = ContactForm(request.POST)
      if fm.is_valid():
        name = fm.cleaned_data['name']
        email = fm.cleaned_data['email']
        mobile_number = fm.cleaned_data['mobile_number']   
        address = fm.cleaned_data['address']
        user = Contact(name=name,email=email,mobile_number=mobile_number,address=address)
        user.save()
        return redirect('/contact/')
        fm = ContactForm()
    else:
    
     fm = ContactForm()
     stud = Contact.objects.all()
     return render(request, 'C/contact.html',{'fm':fm,'stu':stud})
   
   
   








# Logout
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')

# Sigup
def user_signup(request):
 if request.method == "POST":
  form = SignUpForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! You have become an Author.')
   user = form.save()
   group = Group.objects.get(name='Author')
   user.groups.add(group)
 else:
  form = SignUpForm()
 return render(request, 'C/signup.html', {'form':form})

# Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/about/')
  else:
   form = LoginForm()
  return render(request, 'C/login.html', {'form':form})
 else:
  return HttpResponseRedirect('/about/')






# booking page process
def booking_view(request):
  # na = ''
  if request.method == "POST":
    name = request.POST.get('name')
    date = request.POST.get('date')
    email = request.POST.get('email')
    time = request.POST.get('time')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')
    data =Book_ground(name=name,date=date,email=email,time=time,mobile=mobile,address=address)
    
    data.save()

    # na = "Your Detailes Has Been saved Succesfully"
  return render(request, 'C/booking.html',)


# show_detailes process

def show_detailes(request):
  
  
  
  return render(request, 'C/show_detailes.html')



def event_detailes(request):
  return render(request, 'C/event_detailes.html')



def tennis_booking(request):
  
  bk = Book_ground.objects.all()
  return render(request, 'C/tennis_booking.html',{'bk':bk})

