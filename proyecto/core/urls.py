from django.urls import path
from . import views
from .views import HomePageView, SamplePageView, ScannerPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('scanner/', ScannerPageView.as_view(), name='scanner'),
    path('buscar-alumno/', views.view_detalles_alumno, name='view_detalles_alumno'),
    path('detalles-busqueda/', views.detalles_alumno, name='detalles_alumno'),
]

