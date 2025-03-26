
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    
]
