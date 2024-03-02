from django.urls import path
from . import views

app_name = 'conversion'

urlpatterns = [
    path('', views.convert_currency_view, name='convert_currency'),
    path('converter', views.convert_currency_api)
    # Add more URL patterns as needed
]