
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('get-prediction', views.get_Lat_Long),
]
