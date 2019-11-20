from django.conf import settings
from django.http import JsonResponse
from function.encrypt.encrypt import encrypt
from django.utils.deprecation import MiddlewareMixin
import json
import copy

require_encrypt_urls = settings.URL_RES_ENCRYPT


class EncryptMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if isinstance(response, JsonResponse) and request.path_info.lstrip('/corpus/') in require_encrypt_urls:
            iv = request.COOKIES.get('sessionid')[0: 16]
            if not iv:
                return response
            response_copy = copy.deepcopy(response)
            try:
                res = encrypt(response.content, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', '1234567812345678')
                return JsonResponse({
                    'data': str(res)
                })
            except:
                return response_copy
        return response

