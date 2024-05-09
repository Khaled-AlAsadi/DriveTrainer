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

    def test_road_sign_update(self):
        w = self.create_roadsign()
        updated_title = "Updated roadsign title"

        w.title = updated_title
        w.save()

        updated_roadsign_title = RoadSign.objects.get(pk=w.pk)

        self.assertEqual(updated_roadsign_title.title, updated_title)

    def test_road_sign_deletion(self):
        w = self.create_roadsign()
        initial_count = RoadSign.objects.count()
        w.delete()
        self.assertEqual(RoadSign.objects.count(), initial_count - 1)

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

    def test_traffic_rule_deletion(self):
        w = self.create_traficrule()
        initial_count = TraficRule.objects.count()
        w.delete()
        self.assertEqual(TraficRule.objects.count(), initial_count - 1)

    def test_traffic_rule_update(self):
        w = self.create_traficrule()
        updated_title = "Updated traffic rule title"

        w.title = updated_title
        w.save()

        updated_traffic_rule = TraficRule.objects.get(pk=w.pk)

        self.assertEqual(updated_traffic_rule.title, updated_title)
