from django.test import TestCase
from .models import User, HomeResident
# Create your tests here.


class HomeResidentTestCases(TestCase):
    def setUp(self):
        new_users = [
            {
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
                        'phone_number': '+01091238274'
                    }
            },
            {
                'user': {
                    'username': 'TestHomeResident_2',
                    'first_name': 'Test_2',
                    'last_name': 'HomeResident_2',
                    'email': 'home_resident_2@test.com',
                    'password': 'admin'
                },
                'home_resident':
                    {
                        'user': None,
                        'phone_number': '+01091238270'
                    }
            },
            {
                'user': {
                    'username': 'TestHomeResident_3',
                    'first_name': 'Test_3',
                    'last_name': 'HomeResident_3',
                    'email': 'home_resident_3@test.com',
                    'password': 'admin'
                },
                'home_resident':
                    {
                        'user': None,
                        'phone_number': '+01091238271'
                    }
            },
            {
                'user': {
                    'username': 'TestHomeResident_4',
                    'first_name': 'Test',
                    'last_name': 'HomeResident',
                    'email': 'home_resident_4@test.com',
                    'password': 'admin'
                },
                'home_resident':
                    {
                        'user': None,
                        'phone_number': '+01091238272'
                    }
            },
        ]
        for new_user in new_users:
            user = User.objects.create_user(**new_user['user'])
            new_user['home_resident']['user'] = user
            HomeResident.objects.create(**new_user['home_resident'])

    def testGetAllHomeResidents(self):
        phone_numbers_user_names = {
            'TestHomeResident': '+01091238274',
            'TestHomeResident_2': '+01091238270',
            'TestHomeResident_3': '+01091238271',
            'TestHomeResident_4': '+01091238272'
        }

        current_home_residents = HomeResident.objects.all()
        for home_resident in current_home_residents:
            self.assertEqual(home_resident.phone_number, phone_numbers_user_names[home_resident.user.username])

    def testGetHomeResidentByUsername(self):
        test_home_resident = HomeResident.objects.get(user__username='TestHomeResident')
        self.assertEqual('+01091238274', test_home_resident.phone_number)

    def testGetHomeResidentByPhoneNumber(self):
        test_home_resident = HomeResident.objects.get(phone_number='+01091238274')
        self.assertEqual(test_home_resident.user.username, 'TestHomeResident')

    def testUpdateHomeResidentPhoneNumber(self):
        test_home_resident = HomeResident.objects.get(phone_number='+01091238274')
        test_home_resident.phone_number = '+01091238279'
        test_home_resident.save()
        self.assertEqual(test_home_resident.phone_number, '+01091238279')