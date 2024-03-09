from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('',views.index, name='criar'),
    path('update/',views.index, name='update'),
    path('login/',views.index, name='login'),
    path('logout/',views.index, name='logout'),
]