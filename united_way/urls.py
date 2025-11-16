"""
URL configuration for united_way project.

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
from united_way_application import views

urlpatterns = [
    path('', views.home, name='home'),
    path('claim/', views.claim_money, name='claim_money'),
    path("payment/<int:claim_id>/", views.payment_page, name='payment_page'),
    path("verify_code/<int:claim_id>/", views.verify_code_page, name="verify_code_page"),


    path('admin/', admin.site.urls),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
]
