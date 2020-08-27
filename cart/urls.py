from django.urls import path
from cart import views
urlpatterns = [
				path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
				path('pro_details/',views.pro_details,name='pro_details'),	

]