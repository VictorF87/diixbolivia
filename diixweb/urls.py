from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.RegistrarVotante.as_view(), name="login"),
    path('validar', views.validar, name="validar"),
    path('home', views.home, name="home"),
    path('info', views.info, name="info"),
    path('timeline', views.timeline, name="timeline"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
