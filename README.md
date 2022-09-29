# 📋목차

1. tts-input-service
2. 구현사항
3. 기술 스택
4. API Endpoints
5. ERD
6. 참조 문서

<br>

---

# 1. Investment-service
- 설명: TTS input 텍스트 유효성 및 CRUD 관리 서비스
- 개발 기간: 2022.09.22 ~ 2022.09.28

<br>

---


# 2. 구현 사항


## 1) 로그인, 회원가입

- SimpleJWT를 사용하여 로그인 프로세스 구현.
- 로그인 시 access_token과 refresh_token 발급.

<br>

## 2) 프로젝트 CRUD API

- 프로젝트 생성: 
    - 프로젝트 생성 시 음성 파일 생성.
    - 텍스트 전처리:
        - [. ! ?]를 구분자로 하여 문장을 구분.
        - 한글, 영어, 숫자, 물음표, 느낌표, 마침표, 따옴표, 공백을 제외한 나머지 문장은 포함하지 않도록 전처리.
        - 문장의 앞, 뒤에 공백이 존재할 경우 공백 제거
    - response: [('id1' ,'text1'), ('id2', 'text2'), ....]
- 텍스트 조회:
    - pagination: 한 페이지에 10개의 문장을 조회 가능.
- 텍스트 수정: 여러 문장의 텍스트와 스피드를 수정.

<br>

---

# 3. 기술 스택
Language | Framwork | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | 
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 


<br>

---

# 4. API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /api/users/signup/  | POST   | 회원가입 |  useranme: str <br> password: str <br> email: str  | user_id <br> username <br> email |
| /api/users/signin/ | POST   | 로그인 |  useranme: str <br> password: str  | access_token <br> refresh_token |
| /api/users/<int:pk>/  | DELETE   | 계정 삭제 |  없음  | 계정 삭제 성공 여부 |
| /api/projects/  | POST   | 프로젝트 생성 |  project_title: str <br> speed: int <br> text: array of str | project_title <br> text_list|
| /api/projects/<int:pk>/   | GET   | 텍스트 조회 |  없음 | 텍스트, 식별자 |
| /api/projects/<int:pk>/   | PUT   | 프로젝트 수정 |  speed: int <br> text_ids: array of int <br> text_list: array of str <br> | 텍스트, 식별자 |
| /api/projects/<int:pk>/   | DELETE   | 프로젝트 삭제 |  없음 | 프로젝트 삭제 성공 여부 |

<br>

---

# 5. ERD
![](https://user-images.githubusercontent.com/65996045/192437701-f49d5761-a761-4874-9e15-efe850382683.png)

<br>

---

# 6. 참조 문서
- [Postman API Docs](https://documenter.getpostman.com/view/21254145/2s83eyrGyY)
- [프로젝트 회고](https://velog.io/@chaduri7913/tts-input-service-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)
