"""FirstBlog URL Configuration

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
from django.conf.urls import patterns, include, url 
from blog import views

urlpatterns = patterns('', 
	
	url(r'^$', 'blog.views.home', name='home'),
	url(r'^index.html', 'blog.views.index', name='index'),
	url(r'^contributors.html', 'blog.views.contributors', name='contributors'),
	url(r'^documents.html', 'blog.views.docs', name='docs'),
	url(r'^contact.html', 'blog.views.contact', name='contact'),
	url(r'^keelcooler.html$', 'blog.views.keelcooler',name='keelcooler'),
	url(r'^result.html$', 'blog.views.formview',name='formview'),
	url(r'^demo_form.asp', 'blog.views.formr', name='formr'),
)
