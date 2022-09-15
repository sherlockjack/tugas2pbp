from django.test import TestCase
from katalog.models import CatalogItem

# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name="Mie Ufo",
            item_price=8000,
            item_stock=40,
            description="mie yang bisa bikin kenyang",
            rating=10,
            item_url="https://www.tokopedia.com/ferryfish/nissin-ufo-mie-rasa-kari-pedas-100gr"
        )

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        mie=CatalogItem.objects.get(
            item_name="Mie Ufo",
            item_price=8000,
            item_stock=40,
            description="mie yang bisa bikin kenyang",
            rating=10,
            item_url="https://www.tokopedia.com/ferryfish/nissin-ufo-mie-rasa-kari-pedas-100gr"
        )

        self.assertEqual(mie.item_name,"Mie Ufo")
        self.assertEqual(mie.item_price,8000)
        self.assertEqual(mie.item_stock,40)
        self.assertEqual(mie.description,"mie yang bisa bikin kenyang")
        self.assertEqual(mie.rating,10)
        self.assertEqual(mie.item_url,"https://www.tokopedia.com/ferryfish/nissin-ufo-mie-rasa-kari-pedas-100gr")