from django.test import TestCase, RequestFactory
from .models import Users, Pereval, Level, Coordinate, Image
from django.contrib.auth.models import AnonymousUser
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase


def create_pereval(self):
    """
    Create a pereval 
    """
    
    return Pereval.objects.create(user=self.user, beauty_title='test', \
                                           title='title-test', other_titles='other_title', \
                                            level=self.level, coord=self.coord, image=self.image)

# Create your tests here.
class ApiModelTest(TestCase):
    """
    Test models, create pereval
    """
    def setUp(self):
        # Setup run before every test method.
        self.user = Users.objects.create(first_name='first-test',
                                             last_name='last-test',
                                             middle_name='middle-test',
                                             email='test@example.com',
                                             phone='+75677897567')
        self.level = Level.objects.create(winter='ddd')
        self.coord = Coordinate.objects.create(latitude='45.444', longitude='23.2345', height='244')
        self.image = Image.objects.create(title='ddf', image='null')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_setUpTestData(self):      
       
        new = create_pereval(self)
        self.assertEqual(new.beauty_title, 'test')


class PersonViewSetTests(APITestCase):
    
    def test_list_pereval(self):
        """
        Test to list all the pereval in the list
        """
        
        url = 'http://127.0.0.1:8000%s'%reverse('list_or_create_pereval')
        
        response = self.client.get(url, format='json')
        json = response.json()
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(json), 4)

    


       
        