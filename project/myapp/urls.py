"""project URL Configuration

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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_category_master_add', views.admin_category_master_add, name='admin_category_master_add'),
    path('admin_category_master_view', views.admin_category_master_view, name='admin_category_master_view'),
    path('admin_category_master_delete', views.admin_category_master_delete, name='admin_category_master_delete'),

    path('admin_location_master_add', views.admin_location_master_add, name='admin_location_master_add'),
    path('admin_location_master_view', views.admin_location_master_view, name='admin_location_master_view'),
    path('admin_location_master_delete', views.admin_location_master_delete, name='admin_loation_master_delete'),

    path('admin_pic_pool_add', views.admin_pic_pool_add, name='admin_pic_pool_add'),
    path('admin_pic_pool_view', views.admin_pic_pool_view, name='admin_pic_pool_view'),
    path('admin_pic_pool_delete', views.admin_pic_pool_delete, name='admin_pic_pool_delete'),

    path('admin_staff_user_add', views.admin_staff_user_add, name='admin_staff_user_add'),
    path('admin_staff_user_view', views.admin_staff_user_view, name='admin_staff_user_view'),
    path('admin_staff_user_delete', views.admin_staff_user_delete, name='admin_staff_user_delete'),

    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_logout', views.staff_logout, name='staff_logout'),
    path('staff_home', views.staff_home, name='staff_home'),
    path('staff_changepassword', views.staff_changepassword, name='staff_changepassword'),

    path('staff_search_history_add', views.staff_search_history_add, name='staff_search_history_add'),
    path('staff_search_history_view', views.staff_search_history_view, name='staff_search_history_view'),
    path('staff_search_history_delete', views.staff_search_history_delete, name='staff_search_history_delete'),



    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

]
