"""hawkins URL Configuration

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
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
import crud.views as views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('students/', views.Students.as_view(), name='students'),
    path('students/register', views.students_register, name='students_register'),
    path('students/detail', views.students_detail, name='students_detail'),
    path('students/update', views.students_update, name='students_update'),
    path('students/delete', views.students_delete, name='students_delete'),
    path('classes/', views.classes, name='classes'),
    path('settings/', views.settings, name='settings')
)
