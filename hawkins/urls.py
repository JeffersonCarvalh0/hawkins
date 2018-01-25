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
    path('student/list', views.StudentList.as_view(), name='student_list'),
    path('student/register', views.StudentRegister.as_view(), name='student_register'),
    path('student/detail/<slug:registry>', views.StudentDetail.as_view(), name='student_detail'),
    path('student/update/<slug:registry>', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<slug:registry>', views.StudentDelete.as_view(), name='student_delete'),
    path('class/list', views.ClassList.as_view(), name='class_list'),
    path('class/register', views.ClassRegister.as_view(), name='class_register'),
    path('class/detail/<int:pk>', views.ClassDetail.as_view(), name='class_detail'),
    path('class/update/<int:pk>', views.ClassUpdate.as_view(), name ='class_update'),
    path('class/delete/<int:pk>', views.ClassDelete.as_view(), name='class_delete'),
    path('settings/', views.settings, name='settings')
)
