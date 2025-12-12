"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('skills',views.Skills.as_view(),name="skills"),
    path('education',views.Education.as_view(),name="education"),
    path('projects',views.Projects.as_view(),name="projects"),
    path('certificates',views.Certificates.as_view(),name="certificates"),
    path('internships',views.Internships.as_view(),name="internships"),
    path('download-cv',views.DownloadCV.as_view(),name="download_cv"),
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
