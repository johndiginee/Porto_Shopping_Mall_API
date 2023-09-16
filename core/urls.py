"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title = "Porto Shopping Mall API", 
        default_version = "v1",
        description = "Porto Shopping Mall API is an eCommerce store API that allows different software applications to communicate and interact with their platform. This documentation should guide you from the basics (authentication, request structure) to how customers should be using and ordering products (list of products, add to cart etc.).",
        contact = openapi.Contact(email="johndbizz@gmail.com"),
        license = openapi.License(name="MIT License") 
        ),
        public = True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('api/', include('account.urls')),
    path('api/', include('order.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


handler404 = 'utils.error_views.handler404'
handler500 = 'utils.error_views.handler500'

admin.site.site_header = "Porto Shopping Mall API Admin"

admin.site.site_title = "Porto Shopping Mall API Admin Portal"

admin.site.index_title = "Welcome to Porto Shopping Mall API Portal"