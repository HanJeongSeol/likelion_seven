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
    - 
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
