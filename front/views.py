from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductModel
from categories.models import CategoriesModel
from slider.models import SliderModel

# Create your views here.

def index(request):
		slider = SliderModel.objects.all()
		product = ProductModel.objects.all()
		#return HttpResponse(product)
		cat = CategoriesModel.objects.all()
		return render(request,'index.html', {'mycat':cat,'sal':slider,'pro':product})

def about(request):
		return render(request,'about.html')

def registered(request):
		return render(request,'registered.html')

def login(request):
		return render(request,'login.html')

def contact(request):
		return render(request,'contact.html')

def products(request):
		return render(request,'products.html')

def single(request, id):
		#return HttpResponse(id)
		data = ProductModel.objects.get(id=id)
		return render(request,'single.html',{'value':data}) 