from faker import Faker
from rest_framework.test import APITestCase, URLPatternsTestCase

class AbstractAPITest(APITestCase, URLPatternsTestCase):
    
    def setUp(self) -> None:
        self.fake = Faker()
    