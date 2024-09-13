from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    path('category/<str:val>/', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    
    #Login Authentication.
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_View(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
