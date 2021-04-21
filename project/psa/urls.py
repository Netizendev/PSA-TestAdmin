from django.urls import path

from psa import views

app_name = 'psa'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add_provsvar/', views.ProvsvarCreateView.as_view(), name='add_provsvar'),
]