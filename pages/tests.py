from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_home_page_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
