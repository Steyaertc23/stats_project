from django.urls import path
from .views import send_file, generate_records

urlpatterns = [
    path('dl/no-guess/', send_file, name='downloaded'),
    path('', generate_records, name='generate_records')
]