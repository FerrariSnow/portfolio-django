from django.urls import path
from blog import views

from .views import (
    PostView,
    PostDetail
)

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
