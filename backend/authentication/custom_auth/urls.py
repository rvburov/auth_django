from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomPasswordResetView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
