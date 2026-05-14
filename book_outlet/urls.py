from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),        
    path("<int:pk>", views.detail_id, name="detail_id"),
    path("<int:pk>/<slug:url>", views.detail, name="detail"),    
]
