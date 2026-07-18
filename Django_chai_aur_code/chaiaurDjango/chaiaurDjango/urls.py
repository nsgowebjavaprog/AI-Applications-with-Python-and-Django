from django.contrib import admin
from django.urls import path
# import views file
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # By cdoer
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),  # http://127.0.0.1:8000/about/
    # path('contact/', views.contact, name='contact'),
]