"""sarsum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.suministros.viewstotal.inicio import InicioVista

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^table/', include('table.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^$', InicioVista.as_view(), name="inicio"),
    url(r'^vista/', include("apps.vista.urls", namespace="vista")),
    url(r'^suministros/', include("apps.suministros.urls", namespace="suministros")),
]
