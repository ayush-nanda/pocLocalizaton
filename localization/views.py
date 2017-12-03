import os

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView
from django.utils.translation import ugettext as _, activate


class DisplayHomeView(TemplateView):
    template_name = os.path.join("pages", 'home.html')


class ApiLanguageTest(APIView):
    def get(self, request, format=None):
        output = _("This is R.E.S.T. Api way.")
        return JsonResponse({'data': output})
