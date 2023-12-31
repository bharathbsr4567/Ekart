"""
URL configuration for flipkart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.models import *
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', category_list, name='category_list'),
    path('products/', product_list, name='product_list'),
    path('products/<int:category_id>/',product_list, name='product_list_category'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('user_profile/',user_profile, name='user_profile'),
    path('registration/',register,name='registration'),
    path('user_loggedin',user_loggedin,name='user_loggedin'),
    path('user_profile_edit/',user_profile_edit,name='user_profile_edit'),
    path('product_detail/',product_detail,name='product_detail'),
    path('logout/', user_logout, name='logout'),
    path('myorders/',myorders,name='myorders'),
    path('home/',home,name='home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
