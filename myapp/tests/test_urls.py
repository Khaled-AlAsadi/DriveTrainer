from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index,start_quiz,trafic_rules,continue_quiz,road_signs_page,trafic_rule_question_detail,next_question,previous_question,create_roadSign_view,delete_roadSign_view,update_roadSign_view,create_traficrule_view,delete_traficrule_view,update_traficRule_view

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func,index)

    def test_start_quiz_url_resolves(self):
        url = reverse("start_quiz")
        self.assertEqual(resolve(url).func,start_quiz)
    
    def test_trafic_rules_url_resolves(self):
        url = reverse("trafic_rules")
        self.assertEqual(resolve(url).func,trafic_rules)
    
    def test_trafic_rule_create_url_resolves(self):
        url = reverse("trafic_rule/create")
        self.assertEqual(resolve(url).func,create_traficrule_view)
    
    def test_trafic_rule_delete_url_resolves(self):
        url = reverse("traficrule_delete",args=[1])
        self.assertEqual(resolve(url).func,delete_traficrule_view)
    
    def test_trafic_rule_update_url_resolves(self):
        url = reverse("update_traficRule_view",args=[1])
        self.assertEqual(resolve(url).func,update_traficRule_view)
    

    def test_continue_quiz_url_resolves(self):
        url = reverse("continue_quiz")
        self.assertEqual(resolve(url).func,continue_quiz)
       
    def test_road_signs_page_url_resolves(self):
        url = reverse("road_signs")
        self.assertEqual(resolve(url).func,road_signs_page)
    
    def test_road_signs_create_url_resolves(self):
        url = reverse("road_signs/create")
        self.assertEqual(resolve(url).func,create_roadSign_view)
    

    def test_trafic_rule_question_detail_url_resolves(self):
        url = reverse("trafic_rule_question_detail",args=[1])
        self.assertEqual(resolve(url).func,trafic_rule_question_detail)
    
    def test_next_question_url_resolves(self):
        url = reverse("next_question",args=[1])
        self.assertEqual(resolve(url).func,next_question)
    
    def test_previous_question_url_resolves(self):
        url = reverse("previous_question",args=[1])
        self.assertEqual(resolve(url).func,previous_question)
    
    def test_delete_road_sign_url_resolves(self):
        url = reverse("roadsign_delete",args=[1])
        self.assertEqual(resolve(url).func,delete_roadSign_view)
    
    def test_update_road_sign_url_resolves(self):
        url = reverse("update_roadSign_view",args=[1])
        self.assertEqual(resolve(url).func,update_roadSign_view)
    