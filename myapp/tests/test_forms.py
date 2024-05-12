from django.test import SimpleTestCase
from myapp.forms import RoadSignForm, TraficRuleForm


class TestForms(SimpleTestCase):
    def test_roadsign_form_valid_data(self):
        form = RoadSignForm(data={
            "title": "roadsign 1",
            "description": "roadsign 1 description",
            "image_link": "firstimagelink.png"
        })

        self.assertTrue(form.is_valid())

    def test_roadsign_form_no_data(self):
        form = RoadSignForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_traficrule_form_valid_data(self):
        form = TraficRuleForm(data={
            "title": "trafic rule 1",
            "sub_title": "This is the first trafic rule description",
            "sub_text": "This is the first trafic rule sub_text",
            "image_link": "firstimagelinkfortraficrule.png"
        })
        self.assertTrue(form.is_valid())

    def test_traficrule_form_no_data(self):
        form = RoadSignForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
