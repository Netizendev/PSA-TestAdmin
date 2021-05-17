from django.urls import path

from psa import views

app_name = 'psa'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('provsvar/<int:pk>/', views.ProvsvarDetail.as_view(), name='provsvar_detail'),
    path('patient/<int:pk>/', views.PatientDetail.as_view(), name='patient_detail'),
    path('add_provsvar/', views.ProvsvarCreateView.as_view(), name='add_provsvar'),
    path('add_patient/', views.PatientCreateView.as_view(), name='add_patient'),
    path('hantera/<int:pk>/', views.HanteraDetail.as_view(), name='hantera_detail'),
]

