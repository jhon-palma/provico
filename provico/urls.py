"""provico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app.views import index
from app.views import registrousu
from app.views import informeusu
from app.views import informeben
from app.views import registroben
from app.views import registrobenAjax
from app.views import login
from app.views import search

urlpatterns = [
	url(r'^$', index , name='index'),
    url(r'^registrousu$', registrousu, name='registrousu'),
    url(r'^informeusu$', informeusu, name='informeusu'),
    url(r'^informeben$', informeben, name='informeben'),
    url(r'^registroben$', registroben, name='registroben'),
    url(r'^registrobenAjax$', registrobenAjax, name='registrobenAjax'),
    url(r'^login$', login, name='login'),
    url('^search$', search, name='search'),
    url(r'^admin/', admin.site.urls),

]
