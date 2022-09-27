import jwt
import os

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import *


class SignupTests(APITestCase):
    """회원가입 테스트"""
    def test_signup_success(self):
        """
        201: 회원가입 성공 케이스 
        """
        url = reverse('signup')
        data = {
            'username': 'test1',
            'password': '12341234',
            'email': 'test@test.com'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test1')


    def test_signup_password_validation_fail(self):
        """
        400: 회원가입 비밀번호 8자 미만 실패 케이스
        """
        url = reverse('signup')
        data = {
            'username': 'test1',
            'password': '1234',
            'email': 'test@test.com'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_signup_keyerror_fail(self):
        """
        400: 회원가입 key error 실패 케이스
        """
        url = reverse('signup')
        data = {
            'usernam': 'test1',
            'password': '12341234',
            'email': 'test@test.com'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SigninTests(APITestCase):
    """로그인 테스트"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="test1",
            password="12341234",
            email='test@test.com'
            )


    def test_signin_success(self):
        """
        201: 로그인 성공 케이스 
        """
        url = reverse('signin')
        data = {
            'username': 'test1',
            'password': '12341234'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_signin_id_validation_fail(self):
        """
        400: 아이디 불일치 케이스
        """
        url = reverse('signin')
        data = {
            'username': 'test',
            'password': '12341234'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual( 
            response.json(),
            {'messsage': ['아이디를 잘못 입력했습니다.']}
        )


    def test_signin_password_validation_fail(self):
        """
        400: 비밀번호 불일치 케이스
        """
        url = reverse('signin')
        data = {
            'username': 'test1',
            'password': '1234123'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual( 
            response.json(),
            {'messsage': ['비밀번호를 잘못 입력했습니다.']}
        )


class ProjectTests(APITestCase):
    """프로젝트 CRUD 테스트"""
    def setUp(self):
        self.user = User.objects.create_user(
            username="test1",
            password="12341234",
            email='test@test.com'
            )
        self.project = Project.objects.create(
            id = 1,
            project_title='test1',
            user = self.user
            )
        self.audio = Audio.objects.create(
            id = 1,
            audio_file = '1.wav',
            speed = 1,
            project = self.project
            )
        self.text = Text.objects.create(
            id = 1,
            text = '안녕하세요!',
            idx = 1,
            audio = self.audio
        )

    
    def test_post_success(self):
        """
        201: 프로젝트 생성 성공 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        token = response.data['access_token']
        url = reverse('project-c')
        data = {
            'project_title': 'test2',
            'speed': 1.5,
            'text': ["Hi. Bro. Good for you. You Too! What? I am good."]
        }
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.post(
            url, 
            data,
            **headers,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_post_key_error_fail(self):
        """
        400: Key error 실패 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        token = response.data['access_token']
        url = reverse('project-c')
        data = {
            'project_tit': 'test2',
            'speed': 1.5,
            'text': ["Hi. Bro. Good for you. You Too! What? I am good."]
        }
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.post(
            url, 
            data,
            **headers,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_put_success(self):
        """
        200: 프로젝트 수정 성공 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        token = response.data['access_token']
        url = '/api/projects/1/'
        data = {
            'speed': 3,
            'text_ids': [1],
            'text_list': ['Bye']
        }
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.put(
            url, 
            data,
            **headers,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_put_key_error_fail(self):
        """
        400: Key error 실패 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        token = response.data['access_token']
        url = '/api/projects/1/'
        data = {
            'speedo': 3, # speedo로 key error 발생
            'text_ids': [1],
            'text_list': ['Bye']
        }
        headers = {
            'HTTP_AUTHORIZATION': token
        }
        response = self.client.put(
            url, 
            data,
            **headers,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_get_success(self):
        """
        200: 프로젝트 조회 성공 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        url = '/api/projects/1/'
        response = self.client.get(
            url, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_no_object_fail(self):
        """
        404: 클라이언트 없는 객체 조회 실패 케이스
        """
        response = self.client.post(
            reverse('signin'),
            data = {
            'username': 'test1',
            'password': '12341234'
            },
            format='json'
        )
        url = '/api/projects/2/' # project_id가 1인 객체만 있음
        response = self.client.get(
            url, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)