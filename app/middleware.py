from django.utils.translation import activate
from django.conf import settings

class CustomLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 根据您的逻辑判断是否应该更改语言
        if not request.path_info.startswith('/en/'):
            activate(settings.LANGUAGE_CODE)
        
        response = self.get_response(request)
        return response