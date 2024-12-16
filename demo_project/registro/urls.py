from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_persona, name='registrar'),
    path('success/', views.success, name='success'),  # Nueva ruta para éxito
]
