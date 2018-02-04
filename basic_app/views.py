from django.shortcuts import render
from basic_app.forms import UserForm


#from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView,DetailView,CreateView
from . import models

# Create your views here.
#class based view
class CompanyListView(ListView):
	context_object_name = 'company_list' 
	model=models.Company
	template_name = 'basic_app/home.html'

class CompanyAddView(CreateView):
	fields=('name','ceoname','location')
	model=models.Company

def addsuccess(request):
	return render(request,'basic_app/addsuccess.html')

#Function Based view
def index(request):
	return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))
	
def about(request):
	return render(request,'basic_app/about.html')

def contact(request):
	return render(request,'basic_app/contact.html')

def home(request):
	return render(request, 'basic_app/home.html')

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				return HttpResponse("Account not Active")
		else:
			print("Someone tried to login")

			return HttpResponse("Invalid login details")
	else:
		return render(request, 'basic_app/login.html',{})



def register(request):
	registered=False

	if request.method=="POST":
		user_form=UserForm(data=request.POST)

		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()

			registered=True
		else:
			print(user_form.errors)
	else:
		user_form=UserForm()

	return render(request, 'basic_app/register.html',{'user_form':user_form,'registered':registered})