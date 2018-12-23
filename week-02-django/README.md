# 독립환경 설정 (Virtual Environment)

1. Virtualenv 라이브러리 설치하기: pip install Virtualenv
2. 프로젝트 폴더 생성: mkdir {{ python_project }}
3. 프로젝트 폴더 들어가기: cd {{ python_project }}
4. 독립환경 만들기: python -m venv {{ my_python }}
5. 독립환경 실행 시키기: {{ my_python }}\scripts\activate

장고 설치

1. 장고 설치하기: pip install django==1.10.4
2. 새로운 프로젝트 만들기: django-admin startproject {{firstsite}}
3. 기본 데이터베이스 설정하기: python manage.py migrate
4. 로컬 서버 시작하기: python manage.py runserver





- pip 공식문서: <https://pip.pypa.io/en/stable/user_guide/>
- 장고 공식문서: <https://docs.djangoproject.com/en/1.10/>

**https://docs.djangoproject.com/en/1.10/intro/tutorial01/**

**pip 주요 명령어**

- pip install : pip로 파이썬 패키지(라이브러리) 설치하기
- pip uninstall : pip로 파이썬 패키지(라이브러리) 삭제하기
- pip freeze : pip로 설치한 파이썬 패키지(라이브러리) 목록 표시
- pip freeze > requirements.txt : 위의 목록을 requirements.txt 라는 파일로 만들기
- pip install -r requirements.txt : requirements.txt 안의 패키지 전체 설치하기



**cmd**

```
(django_sample) C:\Users\leeap\dev\coding-for-test\week-02-django\src>python manage.py runserver

ctrl+C

$ python manage.py migrate

(django_sample) C:\Users\leeap\dev\coding-for-test\week-02-django\src>python manage.py startapp blog



```

