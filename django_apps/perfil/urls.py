from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    path('',views.criar_perfil, name='criar_perfil'),
    path('update/',views.update, name='update'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_, name='logout'),
]