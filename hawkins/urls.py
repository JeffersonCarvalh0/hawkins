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
    path('students/list', views.StudentList.as_view(), name='student_list'),
    path('students/register', views.StudentRegister.as_view(), name='student_register'),
    path('students/detail', views.StudentDetail.as_view(), name='student_detail'),
    path('students/update', views.StudentUpdate.as_view(), name='student_update'),
    path('students/delete', views.StudentDelete.as_view(), name='student_delete'),
    path('classes/list', views.classes_list, name='classes_list'),
    path('classes/register', views.classes_register, name='classes_register'),
    path('classes/detail', views.classes_detail, name='classes_detail'),
    path('classes/update', views.classes_update, name ='classes_update'),
    path('classes/delete', views.classes_delete, name='classes_delete'),
    path('settings/', views.settings, name='settings')
)
