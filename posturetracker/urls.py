from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from tracker.views import EnviosViewSet, ConectadoViewSet, ListView

router = routers.DefaultRouter()
router.register(r'envios', EnviosViewSet)
router.register(r'conectado', ConectadoViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('lista', ListView.as_view()),
    path('', admin.site.urls),
]
