from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
	return render(request, 'Home.html')

def About(request):
	return render(request, 'About.html')

def Contact(request):
	return render(request, 'Contact.html')

def Services(request):
	return render(request, 'Services.html')

def Hotel(request):
	return render(request, 'Hotel.html')

def Form(request):

	return render(request, 'Form.html')

def add(request):
	val1 = int(request.POST["num1"])
	val2 = int(request.POST["num2"])
	res = val1 + val2

	return render(request, 'Result.html',{'result':res})

def Forms(request):
	return render(request,'Forms.html')

def Formsdata(request):
	if request.method == 'POST':
		name = request.POST.post('name')
		email = request.POST.post('email')
		mobile = request.POST.post('mobile')
		salary = request.POST.post('salary')
		address = request.POST.postt('address')
		data = [name,email,mobile,salary,address]
		return HttpResponse(data)

		if form.is_valid():
			Forms.save()
			return HttpResponse('data inserted')
		else:
			return HttpResponse('error')
	else:
		Forms = DemoForm()
		return render(request,'Forms.html',{'Forms':Forms}) 
