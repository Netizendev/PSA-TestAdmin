from django.urls import path

from . import views

app_name = 'sample'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sample_id>/', views.detail, name='detail'),
]