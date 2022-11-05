from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.


@api_view(['POST'])
@ensure_csrf_cookie
def login(request):
    user_creds = request.data
    return Response(user_creds, status=status.HTTP_200_OK)