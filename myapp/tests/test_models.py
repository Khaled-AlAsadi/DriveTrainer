from django.test import TestCase
from myapp.models import RoadSign, TraficRule


class TestModels(TestCase):

    def create_roadsign(self, title="The first Roadsign title",
                        description="The first Roadsign description",
                        image_link="The first Roadsign imagelink"):
        return RoadSign.objects.create(
            title=title, description=description, image_link=image_link)

    def test_roadsign_creation(self):
        w = self.create_roadsign()
        self.assertEqual(w.title, "The first Roadsign title")

    def create_traficrule(self, title="The first trafic rule title",
                          sub_title="The first trafic rule sub title",
                          sub_text="The first trafic rule sub text",
                          image_link="The first trafic rule image link"):
        return TraficRule.objects.create(title=title,
                                         sub_title=sub_title,
                                         sub_text=sub_text,
                                         image_link=image_link)

    def test_traficrule_creation(self):
        w = self.create_traficrule()
        self.assertEqual(w.title, "The first trafic rule title")
