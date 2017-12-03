from django.conf.urls.i18n import is_language_prefix_patterns_used
from django.middleware.locale import LocaleMiddleware

from django.conf import settings
from django.utils import translation


class LocaleCustomMiddleware(LocaleMiddleware):

    def process_request(self, request):

        language_code = request.META.get(settings.LANGUAGE_CODE_HEADER_NAME, settings.LANGUAGE_CODE)
        if language_code not in dict(settings.LANGUAGES):
            language_code = settings.LANGUAGE_CODE

        urlconf = getattr(request, 'urlconf', settings.ROOT_URLCONF)
        i18n_patterns_used, prefixed_default_language = is_language_prefix_patterns_used(urlconf)
        language = translation.get_language_from_request(request, check_path=i18n_patterns_used)
        language_from_path = translation.get_language_from_path(request.path_info)

        if not language_from_path and i18n_patterns_used and not prefixed_default_language:
            language = language_code
        if language == 'en' and language_code != 'en':
            language = language_code
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()
