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

    - 저장된 데이터를 사용자에게 보여주기 위한 과정
        ```
        1. views.py에서 쿼리셋 생성
        2. html파일에서 쿼리셋 메소드를 사용하여 데이터를 불러온다.
            -> 메소드의 종류는 다양하기 때문에 구글링해보기.
        3. 담겨진 데이터가 다양할 때 for문을 사용하여 차례대로 불러온다.
        ```
    ```

## Blog Project
---
### 개요
1. Model을 활용하여 간단한 Blog를 만들어 보자.
2. 메인 페이지에 보여지는 글자 수 제한 기능 추가
3. '...more'에 상세 페이지로 이동할 수 있는 링크 달기
4. 링크를 클릭했을 때 detail.html페이지 내보내기
