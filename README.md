# ๐๋ชฉ์ฐจ

1. tts-input-service
2. ๊ตฌํ์ฌํญ
3. ๊ธฐ์  ์คํ
4. API Endpoints
5. ERD
6. ์ฐธ์กฐ ๋ฌธ์

<br>

---

# 1. Investment-service
- ์ค๋ช: TTS input ํ์คํธ ์ ํจ์ฑ ๋ฐ CRUD ๊ด๋ฆฌ ์๋น์ค
- ๊ฐ๋ฐ ๊ธฐ๊ฐ: 2022.09.22 ~ 2022.09.28

<br>

---


# 2. ๊ตฌํ ์ฌํญ


## 1) ๋ก๊ทธ์ธ, ํ์๊ฐ์

- SimpleJWT๋ฅผ ์ฌ์ฉํ์ฌ ๋ก๊ทธ์ธ ํ๋ก์ธ์ค ๊ตฌํ.
- ๋ก๊ทธ์ธ ์ access_token๊ณผ refresh_token ๋ฐ๊ธ.

<br>

## 2) ํ๋ก์ ํธ CRUD API

- ํ๋ก์ ํธ ์์ฑ: 
    - ํ๋ก์ ํธ ์์ฑ ์ ์์ฑ ํ์ผ ์์ฑ.
    - ํ์คํธ ์ ์ฒ๋ฆฌ:
        - [. ! ?]๋ฅผ ๊ตฌ๋ถ์๋ก ํ์ฌ ๋ฌธ์ฅ์ ๊ตฌ๋ถ.
        - ํ๊ธ, ์์ด, ์ซ์, ๋ฌผ์ํ, ๋๋ํ, ๋ง์นจํ, ๋ฐ์ดํ, ๊ณต๋ฐฑ์ ์ ์ธํ ๋๋จธ์ง ๋ฌธ์ฅ์ ํฌํจํ์ง ์๋๋ก ์ ์ฒ๋ฆฌ.
        - ๋ฌธ์ฅ์ ์, ๋ค์ ๊ณต๋ฐฑ์ด ์กด์ฌํ  ๊ฒฝ์ฐ ๊ณต๋ฐฑ ์ ๊ฑฐ
    - response: [('id1' ,'text1'), ('id2', 'text2'), ....]
- ํ์คํธ ์กฐํ:
    - pagination: ํ ํ์ด์ง์ 10๊ฐ์ ๋ฌธ์ฅ์ ์กฐํ ๊ฐ๋ฅ.
- ํ์คํธ ์์ : ์ฌ๋ฌ ๋ฌธ์ฅ์ ํ์คํธ์ ์คํผ๋๋ฅผ ์์ .

<br>

---

# 3. ๊ธฐ์  ์คํ
Language | Framwork | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | 
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 


<br>

---

# 4. API Endpoints
| endpoint | HTTP Method | ๊ธฐ๋ฅ   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /api/users/signup/  | POST   | ํ์๊ฐ์ |  useranme: str <br> password: str <br> email: str  | user_id <br> username <br> email |
| /api/users/signin/ | POST   | ๋ก๊ทธ์ธ |  useranme: str <br> password: str  | access_token <br> refresh_token |
| /api/users/<int:pk>/  | DELETE   | ๊ณ์  ์ญ์  |  ์์  | ๊ณ์  ์ญ์  ์ฑ๊ณต ์ฌ๋ถ |
| /api/projects/  | POST   | ํ๋ก์ ํธ ์์ฑ |  project_title: str <br> speed: int <br> text: array of str | project_title <br> text_list|
| /api/projects/<int:pk>/   | GET   | ํ์คํธ ์กฐํ |  ์์ | ํ์คํธ, ์๋ณ์ |
| /api/projects/<int:pk>/   | PUT   | ํ๋ก์ ํธ ์์  |  speed: int <br> text_ids: array of int <br> text_list: array of str <br> | ํ์คํธ, ์๋ณ์ |
| /api/projects/<int:pk>/   | DELETE   | ํ๋ก์ ํธ ์ญ์  |  ์์ | ํ๋ก์ ํธ ์ญ์  ์ฑ๊ณต ์ฌ๋ถ |

<br>

---

# 5. ERD
![](https://user-images.githubusercontent.com/65996045/192437701-f49d5761-a761-4874-9e15-efe850382683.png)

<br>

---

# 6. ์ฐธ์กฐ ๋ฌธ์
- [Postman API Docs](https://documenter.getpostman.com/view/21254145/2s83eyrGyY)
- [ํ๋ก์ ํธ ํ๊ณ ](https://velog.io/@chaduri7913/tts-input-service-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)
