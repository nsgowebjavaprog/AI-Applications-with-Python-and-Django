from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # Added by me [programmer / cdoer / Nagaraj-Loni]
    path('', include('calc.urls')),
    # Default
    path("admin/", admin.site.urls),
]