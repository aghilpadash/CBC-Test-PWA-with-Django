from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CBC/', views.CBC_test, name='CBC'),
    path('CBC/result/', views.cbc_result, name='cbc_result'),
    url(r'^serviceworker(.*.js)$', views.serviceworker, name='serviceworker'),
    url(r'^patient/all/$', views.AllPatientAPIView.as_view(), name='patients'),
    url(r'^ecg/submit/$', views.SubmitEcgAPIView.as_view(), name='submit_ecg'),
    url(r'^CBC/submit/$', views.SubmitCBCAPIView.as_view(), name='submit_CBC'),
    url(r'^heartattack/submit/$', views.SubmitHeartAttackAPIView.as_view(), name='submit_heart_attack'),
    url(r'^patient/submit/$', views.SubmitPatientAPIView.as_view(), name='submit_patient'),
]
