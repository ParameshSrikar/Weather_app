from django.contrib import admin
from django.urls import path
from weather import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Adjust this to match your view name
]
