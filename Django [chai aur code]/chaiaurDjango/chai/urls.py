from django.contrib import admin
from django.urls import path
# import views file
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    # By cdoer
    path('', views.all_chai, name='all_chai'),
]