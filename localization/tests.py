import json
import os
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.utils.translation import activate


class TemplateTestCase(TestCase):
    def test_uses_home_template(self):
        activate('en')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, os.path.join("pages", 'home.html'))


class InternationalizationTestCase(TestCase):
    client = Client()

    def test_internationalization(self):
        for lang, text in [('en', 'Welcome to Webshar!'),
                           ('fr', 'Bienvenue à Webshar!')]:
            activate(lang)
            response = self.client.get(reverse("home"), {}, HTTP_LANGUAGE_CODE=lang)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, text)

    def test_internationalization_api(self):
        for lang, text in [('en', 'This is R.E.S.T. Api way.'),
                           ('fr', "C'est R.E.S.T. Fa\u00e7on Api.")]:
            activate(lang)
            response = self.client.get(reverse("testApi"), {}, HTTP_LANGUAGE_CODE=lang)
            self.assertEqual(response.status_code, 200)
            self.assertJSONEqual(response.content, {"data": text})
