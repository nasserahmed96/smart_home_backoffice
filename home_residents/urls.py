from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)
from .views import get_user_details

urlpatterns = [
    path('authenticate', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user', get_user_details, name='get_user_details')
]
