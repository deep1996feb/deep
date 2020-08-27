from django.urls import path
from front import views
from myproject import settings
from django.conf.urls.static import static

urlpatterns = [
	
		path('',views.index, name='index'),
		path('about/', views.about, name='about'),
		path('register/', views.registered, name='registered'),
		path('login/', views.login, name='login'),
		path('contact/', views.contact, name='contact'),
		path('product/', views.products, name='products'),
		path('single/<int:id>/',views.single,name='single'),
]
if settings.DEBUG:
	#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)