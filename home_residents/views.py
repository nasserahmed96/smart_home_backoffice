import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework_simplejwt.tokens import AccessToken
from .models import HomeResident

# Create your views here.


@api_view(['POST'])
@ensure_csrf_cookie
def get_user_details(request):
    request_body = request.data
    user = AccessToken(request_body['access'])
    print(type(user))
    print('User: ', user['user_id'])
    home_resident = HomeResident()
    return Response(json.dumps('{user: user_details}'), status=status.HTTP_200_OK)