from django.urls import path, include
from . import views
from .views import header, footer

urlpatterns = [
    path('', views.index_view),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
]
