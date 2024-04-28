from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index,start_quiz,trafic_rules,continue_quiz,road_signs_page

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func,index)

    def test_start_quiz_url_is_resolved(self):
        url = reverse("start_quiz")
        self.assertEqual(resolve(url).func,start_quiz)
    
    def test_trafic_rules_url_is_resolved(self):
        url = reverse("trafic_rules")
        self.assertEqual(resolve(url).func,trafic_rules)
    
    def test_continue_quiz_url_is_resolved(self):
        url = reverse("continue_quiz")
        self.assertEqual(resolve(url).func,continue_quiz)
       
    def test_road_signs_page_url_is_resolved(self):
        url = reverse("road_signs")
        self.assertEqual(resolve(url).func,road_signs_page)
    
