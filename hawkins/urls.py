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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
import crud.views as views

urlpatterns = []

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.Index.as_view(), name='index'),
    path('student/list', views.StudentList.as_view(), name='student_list'),
    path('student/register', views.StudentRegister.as_view(), name='student_register'),
    path('student/detail/<slug:pk>/', views.StudentDetail.as_view(), name='student_detail'),
    path('student/update/<slug:pk>/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<slug:pk>/', views.StudentDelete.as_view(), name='student_delete'),
    path('student/grades/<slug:pk>/', views.EditGrades.as_view(), name='edit_grades'),
    path('class/list', views.ClassList.as_view(), name='class_list'),
    path('class/register', views.ClassRegister.as_view(), name='class_register'),
    path('class/detail/<int:pk>/', views.ClassDetail.as_view(), name='class_detail'),
    path('class/update/<int:pk>/', views.ClassUpdate.as_view(), name='class_update'),
    path('class/delete/<int:pk>/', views.ClassDelete.as_view(), name='class_delete'),
    path('class/add_student/<int:pk>', views.ClassAddStudent.as_view(), name='class_add_student'),
    path('class/<int:class>/remove_student/<int:student>/', views.ClassRemoveStudent.as_view(), name='class_remove_student'),
    path('subject/register/<int:pk>/', views.SubjectRegister.as_view(), name='subject_register'),
    path('subject/delete/<int:class>/<int:pk>/', views.SubjectDelete.as_view(), name='subject_delete'),
    path('settings/', views.Settings.as_view(), {'pk' : 0}, name='settings')
)
