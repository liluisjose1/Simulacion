"""djmaterial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
#from django.urls import reverse



from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
]
admin.site.site_header = _("Farmacia UES-FMO")


urlpatterns += [
    path('', RedirectView.as_view(url='home/', permanent=False)),
    path('home/', include('inventario.urls')),
    path('jet/', include('jet.urls','jet')),
    path('jet/dashboard', include('jet.dashboard.urls','jet-dashboard')),
]
