from django.urls import path, include
from .views import login, new_account

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login, name='login_redirect'),
    path('register/', new_account, name='signup'),
]