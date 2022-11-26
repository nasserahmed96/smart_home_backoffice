from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)
from .views import create_home_resident, get_all_home_residents

urlpatterns = [
    path('authenticate', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('user', get_user_details, name='get_user_details'),
    path('create-home-resident', create_home_resident, name='create_home_resident'),
    path('home-residents', get_all_home_residents, name='get_all_home_residents')
]
