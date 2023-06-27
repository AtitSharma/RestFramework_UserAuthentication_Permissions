"""
URL configuration for api_project project.

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
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("useraccount.urls",namespace="user")),
    path("product/",include("product_details.urls",namespace="product_detail")),
    # path("gettoken/",TokenObtainPairView.as_view(),name="get_token"),
    # path("gettoken/",CustomGetToken.as_view(),name="get_token"),
    path("refreshtoken/",TokenRefreshView.as_view(),name="refresh_token"),
    path("verifytoken/",TokenVerifyView.as_view(),name="verify_token")
]
