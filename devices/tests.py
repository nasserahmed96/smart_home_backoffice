from django.contrib.auth.models import User
import datetime
from django.test import TestCase
from .models import Device, HomeResident

# Create your tests here.
class DeviceTestCases(TestCase):
    def create_root_user(self):
        new_user = {
                    'username': 'rootUser',
                    'first_name': 'Root',
                    'last_name': 'User',
                    'email': 'root_user@test.com',
                    'password': 'admin'
                }
        return User.objects.create_user(**new_user)
    def create_home_resident(self):
        new_user = {
                'user': {
                    'username': 'TestHomeResident',
                    'first_name': 'Test',
                    'last_name': 'HomeResident',
                    'email': 'home_resident@test.com',
                    'password': 'admin'
                },
                'home_resident':
                    {
                        'user': None,
                        'phone_number': '+01091238274',
                    }
            }
        user = User.objects.create_user(**new_user['user'])
        new_user['home_resident']['user'] = user
        return HomeResident.objects.create(**new_user['home_resident'])

    def setUp(self):
        device_identifier = {
            'device_id': '00000000-36ab-9c3c-0000-0000714a4f37',
            'home_resident': self.create_home_resident().id,
            'device_model': 'Samsung A02',
            'brand': 'Samsung',
            'last_online': datetime.datetime.now(),
            'created_by': self.create_root_user().id,
            'created_at': datetime.datetime.now()
        }
        Device.objects.create(**device_identifier)

    def testGetDeviceByHomeResidentId(self):
        device = Device.objects.get(home_resident__id = 1)
        self.assertEqual(device.id, 1)