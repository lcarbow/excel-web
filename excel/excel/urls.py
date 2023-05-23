"""excel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from excel_integration.views import contact_list
from django.urls import path
from excel_integration import views
from excel_integration.views import delete_contact
from excel_integration.views import edit_contact, update_contact
from excel_integration.views import calendar_view
from excel_integration import views as excel_views
from django.urls import path
from django.contrib import admin
from excel_integration import views as integration_views
from excel_integration import views as integration_views

urlpatterns = [
    path('', integration_views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path('contacts/', integration_views.contact_list, name='contact_list'),
    path('contacts/add/', integration_views.add_contact, name='add_contact'),
    path('contacts/<int:kunden_id>/', integration_views.show_contact_info, name='show_contact_info'),
    path('contacts/edit/<int:kunden_id>/', integration_views.edit_contact, name='edit_contact'),
    path('contacts/update/<int:kunden_id>/', integration_views.update_contact, name='update_contact'),
    path('contacts/delete/<int:kunden_id>/', integration_views.delete_contact, name='delete_contact'),
    path('calendar/', integration_views.calendar_view, name='calendar_view'),
    path('login/', integration_views.login_view, name='login'),
    path('map/', integration_views.map_view, name='map_view'),
]

    






