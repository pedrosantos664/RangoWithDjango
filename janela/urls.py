from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)