from django.urls import path
from.import views
urlpatterns =[
path('Home', views.Home, name='Home'),
path('About/', views.About, name='About'),
path('Services/', views.Services, name='Services'),
path('Contact/', views.Contact, name='Contact'),
path('Hotel/', views.Hotel, name= 'Hotel'),
path('Form/', views.Form, name= 'Form'),
path('add/', views.add, name= 'add'),
path('Forms/', views.Forms, name='Forms'),
path('Formsdata/', views.Formsdata, name='Formsdata'),
]