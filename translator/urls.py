from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.translator_view, name='translator_view')
]