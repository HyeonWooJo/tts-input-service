import jwt
import os
import re

from apis.models  import User
from django.http   import JsonResponse
from django.conf import settings

def login_decorator(func):

    def wrapper(self, request, *args, **kwargs):
        try:
            token         = request.headers.get("Authorization", None)
            token_payload = jwt.decode(
                                token, 
                                os.environ.get('SECRET_KEY'), 
                                os.environ.get('ALGORITHM'))
            user          = User.objects.get(id=token_payload['user_id'])
            request.user  = user

            return func(self, request, *args, **kwargs) 

        except jwt.DecodeError:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)
            
    return wrapper  


def text_validation(text):
    """텍스트 유효성 검사"""

    """텍스트에 한글, 영어, 숫자, 물음표, 느낌표, 마침표, 따옴표, 공백 외 다른 문자열 제거"""
    REGEX_TEXT = '[^a-zA-Z가-힣0-9.,?!\"\'\s]'
    text = re.sub(REGEX_TEXT, '', text)

    """맨 앞과 뒤 공백 제거"""
    text = text.strip()

    """.과 ?과 !를 구분자로 텍스트 쪼개기"""
    text = re.split('([.|?|!])', text)

    for i in range(len(text)):
        text[i] = text[i].strip()

    for i in range(len(text)):
        if text[i] in ('.', '?', '!'):
            text[i] += '*'

    text = ''.join(text)
    text = re.split('[*]', text)
    value = []

    for i in range(len(text)):
        if len(text[i]) > 1:
            value.append(text[i])

    return value


def audio_maker(id):
    """음원 생성 함수"""
    file = f'{id}.wav'
    f = open(f'{settings.BASE_DIR}/media/project/{id}.wav', 'w')
    f.close
    return file