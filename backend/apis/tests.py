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
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual( 
            response.json(),
            {'messsage': ['비밀번호를 잘못 입력했습니다.']}
        )