from django.urls import path

from psa import views

app_name = 'psa'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ProvsvarDetail.as_view(), name='detail'),
    path('<int:pk>/', views.HanteraDetail.as_view(), name='prov'),
    path('add_provsvar/', views.ProvsvarCreateView.as_view(), name='add_provsvar'),
    path('add_patient/', views.PatientCreateView.as_view(), name='add_patient'),
]

