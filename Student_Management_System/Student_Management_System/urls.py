"""
URL configuration for Student_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('student_login/', views.student_login , name='student_login'),
    path('admin_login/', views.admin_login , name='admin_login'),
    path('logout/', views.admin_logout , name='admin_logout'),
    path('student_signup/', views.student_signup , name='student_signup'),
    path('student_details/', views.student_details, name="student_details"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update_data/<int:id>/', views.update_data_for_admin, name="update_data_for_admin"),
    path('update_info/<int:id>/', views.update_data_for_student, name="update_data_for_student"),
    path('change_password/<int:id>/', views.change_password, name="change_password"),
    path('changed_details/<str:username>/', views.changed_details, name="changed_details"),
    
]
