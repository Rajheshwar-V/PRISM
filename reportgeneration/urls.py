"""reportgeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dashboard import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.main_dashboard, name="home"),
    path('save-study/', views.save_study, name="save"),
    path('all-studies/', views.all_studies, name="all"),
    path('view-study/<int:study_id>', views.view_study, name="view"),
    path("view-studies/", views.view_study_list, name="study_list")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
