from django.contrib import admin
from django.urls import path

from spending import views

urlpatterns = [
    path('', views.index, name='home'),
    path(r'spending/<cost>/', views.spending, name='spending'),
    path('admin/', admin.site.urls),
]
