from django.urls import path
from . import views
urlpatterns = [
    path('', views.checkall),
    path('dj_api/check/', views.check),
]
