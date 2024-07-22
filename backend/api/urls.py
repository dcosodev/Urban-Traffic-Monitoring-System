from django.urls import path
from . import views

urlpatterns = [
    path('trafficflow/', views.TrafficFlowListCreate.as_view(), name='trafficflow_list_create'),
    path('trafficflow/<int:pk>/', views.TrafficFlowDetail.as_view(), name='trafficflow_detail'),
    path('trafficincident/', views.TrafficIncidentListCreate.as_view(), name='trafficincident_list_create'),
    path('trafficincident/<int:pk>/', views.TrafficIncidentDetail.as_view(), name='trafficincident_detail'),
    path('trafficsensor/', views.TrafficSensorListCreate.as_view(), name='trafficsensor_list_create'),
    path('trafficsensor/<int:pk>/', views.TrafficSensorDetail.as_view(), name='trafficsensor_detail'),
]
