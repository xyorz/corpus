from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

require_login_urls = settings.URL_REQ_LOGIN


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'username' not in request.session or not request.session['username']:
            path = request.path_info.lstrip('/corpus/')
            if path in require_login_urls:
                return JsonResponse({
                    'success': False
                })
        return None
