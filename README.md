# 멋쟁이사자처럼 7기 수업 프로젝트

## 기본 설정
----------------------
- VSCode 설정
    ```
    - ctrl + shift + x로 확장 탭에서 아래 항목 설치
        1. Auto Close Tag
        2. Auto Reaname Tag
        3. Python (필수)
        4. Django 
        5. vscode-icons
    
    - 파일 -> 기본설정 -> 설정 탭에서 encoding 검색 후 utf8을 default로 설정
    ```

- Django 설치
    ```
    - VSCode에서 프로젝트를 진행할 폴더 선택

    - $ python -m pip install django
        ->  django 설치
    ```
- Django 설정
    ```
    - $ python -m venv <가상환경이름>
        -> 가상환경 설치

    - $ source <가상환경이름>/scripts/activate
        -> 가상환경 실행

    - $ django-admin startproject <projcet이름>
        -> 프로젝트 생성

    - $ python manage.py startapp <app이름>
        -> app 생성
        -> app 생성 이전에 만들었던 project로 폴더 변경, cd <project이름>

    - project폴더 -> setting.py의 INSTALLED_APPS부분에 'app이름.apps.app이름Config'추가
        -> 마지막에 쉼표로 끝내야 동작한다.
        -> project에 app등록하는 과정

    - $ python manage.py runserver 
        -> 서버 실행
    ```

## wordcount
----------------
### 설명
- 사용자가 입력한 문장에 사용된 단어의 갯수를 카운팅 하는 페이지.
- home에서 사용자가 문장을 입력할 시 result에서 결과를 확인할 수 있다.


## Model
--------
### 개요
1. Model에 데이터를 어떻게 담을 것인가
2. Model의 데이터를 어떻게 View로 넘길 것인가
3. 그것을 어떻게 화면에 띄울 것인가

- Model 설정
    ```
    - Models.py에 어떤 종류의 데이터를 처리할지 Class로 정의
    
    - $ python mamage.py makemigrations
        -> migration파일 생성하는 과정
    
    - $ python manage.py migrate
        -> 데이터베이스에 적용하는 과정

    - $ python manage.py createsuperuser
        -> admin계정 생성

    - app의 admin.py에 우리가 설정한 models.py를 추가시켜줘야한다.
        -> DB에 우리가 설정한 스키마를 토대로 데이터를 저장시키기 위한 작업
    ```
