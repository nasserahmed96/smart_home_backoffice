import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework_simplejwt.tokens import AccessToken
from .models import HomeResident
from .serializers import HomeResidentSerializer


# Create your views here.


@api_view(['POST'])
@ensure_csrf_cookie
def get_user_details(request):
    user = AccessToken(request.headers['Authorization'].replace('Bearer ', ''))
    home_resident = HomeResident.objects.get(user__id=user['user_id'])
    return Response(HomeResidentSerializer(home_resident, many=False).data, status=status.HTTP_200_OK)


@api_view(['POST'])
@ensure_csrf_cookie
def create_home_resident(request):
    print('Request data: ', request.data)
    serializer = HomeResidentSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_home_residents(request):
    home_residents_serializer = HomeResidentSerializer(HomeResident.objects.all(), many=True)
    return Response(home_residents_serializer.data, status=status.HTTP_200_OK)
