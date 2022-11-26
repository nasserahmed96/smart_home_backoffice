import re
from rest_framework import serializers
from .models import HomeResident, User


class HomeResidentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=15)

    def validate_phone_number(self, phone_number):
        if not re.match("^(\+[0-9]{1,3}){0,1}([0-9]{11,13})$", phone_number):
            raise serializers.ValidationError("Incorrect phone number format, plase use +country_code followed by the phone number")
        return phone_number

    def create(self, validated_data):
        print('Validated data: ')
        print(validated_data)
        home_resident = {
            'user': None,
            'phone_number': validated_data.pop('phone_number')
        }
        new_user = User.objects.create_user(**validated_data)
        home_resident['user'] = new_user
        new_home_resident = HomeResident.objects.create(**home_resident)
        return new_home_resident

    def to_representation(self, instance):
        response = dict()
        response['username'] = instance.user.username
        response['first_name'] = instance.user.first_name
        response['last_name'] = instance.user.last_name
        response['email'] = instance.user.email
        response['phone_number'] = instance.phone_number
        return response

    class Meta:
        model = HomeResident
        exclude = ['user']

