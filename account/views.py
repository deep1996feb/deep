from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
		if request.method == 'POST':
				fname = request.POST['fname']
				lname = request.POST['lname']
				uname = request.POST['username']
				email = request.POST['email']
				password = request.POST['password']
				cpassword = request.POST['cpassword']
				#data = [fname,lname,username,email,password]
				if password == cpassword:
						if User.objects.filter(username=uname).exists():
								messages.info(request,'User Already Exist')
								return redirect('/register/')
						elif User.objects.filter(email=email).exists():
								messgaes.info(request,'Email Already Exist')
								return redirect('/register/')
						else:
								user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=password)
								user.save()
								return HttpResponse('User Created')
				else:
						messages.info(request,'Password did not match')
						return redirect('/register/')
def login(request):
		if request.method == 'POST':
				uname = request.POST['uname']
				password = request.POST['password']
				user = auth.authenticate(username=uname,password=password)
				if user is not None:
						auth.login(request, user)
						return redirect('/')
				else:
						messages.info(request,'Invalid User Name or Password')
						return redirect('/login/')
def logout(request):
		auth.logout(request)
		return redirect('/')

