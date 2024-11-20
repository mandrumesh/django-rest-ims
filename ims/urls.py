"""
URL configuration for ims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from base.views import ProductApiView, ProductTypeApiView, ProductTypeDetailApiView, PurchaseApiView, PurchaseDetailApiView, SellApiView, DepartmentApiView, DepartmentDetailApiView, VendorApiView, VendorDetailApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductApiView.as_view({'get':'list', 'post':'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'})),
    path('product-type/', ProductTypeApiView.as_view()),
    path('product-type/<int:pk>/', ProductTypeDetailApiView.as_view()),
    path('purchase/', PurchaseApiView.as_view()),
    path('purchase/<int:pk>/', PurchaseDetailApiView.as_view()),
    path('sell/', SellApiView.as_view()),
    path('sell/<int:pk>/', SellApiView.as_view()),
    path('department/', DepartmentApiView.as_view()),
    path('department/<int:pk>/', DepartmentDetailApiView.as_view()),
    path('vendor/', VendorApiView.as_view()),
    path('vendor/<int:pk>/', VendorDetailApiView.as_view()),
]
