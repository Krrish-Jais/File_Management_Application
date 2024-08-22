"""
URL configuration for File_Manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
    
Examples:
Function views:
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
Class-based views:
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Login_Page.views import Login_View  # Import the Login view from Login_Page app
from Depart_Dashboard.views import Depart_View  # Import the Department Dashboard view from Depart_Dashboard app
from Super_Dashboard.views import Super_View  # Import the Super Dashboard view from Super_Dashboard app
from Document_Details.views import Document_View  # Import the Document Details view from Document_Details app

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin interface
    path('login/', Login_View),  # URL pattern for the login page
    path('depart/<str:OID>/<str:Depart>/', Depart_View),  # URL pattern for the department dashboard
    path('super/<str:OID>/', Super_View),  # URL pattern for the super dashboard
    path('document/<str:OID>/<str:DocumentID>/', Document_View),  # URL pattern for the document details page
]
