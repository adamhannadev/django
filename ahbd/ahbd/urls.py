"""
URL configuration for ahbd project.

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
from django.urls import path
from bookings.views import calendar, home
from progress import views as progress_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", progress_views.main),
    path("progress/new-figure", progress_views.new_figure),
    path("progress/show/<int:id>", progress_views.show),
    path("progress/list/", progress_views.list),
    path("week/", calendar)
]
