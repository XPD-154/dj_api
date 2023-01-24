from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('dj_api/checkall/', views.checkall),
    path('dj_api/check/', views.check),
]
