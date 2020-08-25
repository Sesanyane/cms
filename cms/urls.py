"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from contract.admin_site import contract_admin
from django.apps import apps as django_apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from django.views.generic.base import RedirectView

app_name = 'cms'
app_config = django_apps.get_app_config(app_name)

urlpatterns = [
    path('administrator/', contract_admin.urls),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='administrator/'), name='home_url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
