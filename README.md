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
    4-1. detail.html은 하나만 생성하여 x번째 객체를 요청하면 x번 객체의 내용을 보여준다.
    4-2. 페이지의 url설계를 사용한다.(사이트/blog/객체번호)
    4-3. 객체번호 즉 객체가 존재하지 않는다면 404에러 표시.

- 용어정리
    1. pk(primary key) : 객체들의 이름표, 구분자, 데이터의 대표값
    2. path converter : URL을 게층적으로 디자인하여 편의성을 제공해준다.
    3. get_object_or_404(클래스,검색조건) : 두 개의 인자를 받는 클래스, 어떤 클래스에서 검색조건에 해당되는 데이터가 있다면 가져오고, 없다면 404에러를 표시해준다.

- Model.py
    ```python
    - Model에서 생성한 클래스에 함수 추가
        ->  def summary(self):
                return self.body[:100]  
        -> summary를 호출하게되면 body의 글자수를 100자로 제한하여 사용자에게 보여주게 된다.
    ```

- Views.py
    ```python
    - 사용자에게 자세한 내용을 보여주는 detail 함수 추가
        -> get_object_or_404를 사용하기 위해서는 import먼저 해야한다.
    ```
- url.py
    ```python
    - detail를 보여주는 url 추가
        -> path('blog/<int:blog_id>',blog.views.detail, name='detail'),
        -> int형 blog_id가 detail로 넘어간다.
        -> blog_id가 pk이며 path converter가 이루어지도록 한다.
        -> 페이지 별 넘버링을 통하여 계층적으로 관리할 수 있도록 한다.
    ```

## portfolio
---
### 설명
- Django에서 여러가지 파일을 사용하여 개인 포트폴리오 사이트 제작

### 용어정리
- Static File(정적파일) : 미리 서버에 저장되어있는 파일, 서버에 저장된 그대로를 서비스해주는 파일
    1. 프로젝트 입장에서 이미 뭔지 아는 파일, 개발할 때 미리 준비해둔 파일 = "static"
    2. 웹 서비스 이용자들이 업로드하는 파일 = "media"
- Dynamic File(동적파일) : 서버의 데이터들이 어느정도 가공된 다음 서비스되는 파일.(상황에 따라 받는 파일이 달라질 수 있다.)

### 정적파일 사용하여 포트폴리오 만들기.
- Static 다루기 : 미리 준비해둔 사진 띄우기
- Media 다루기 : 사진 업로드 해보기
- Static 파일의 처리 과정
    1. Static 파일들의 위치 찾기
    2. Static 파일들을 한 곳에 모으기
- 우리가 할 일
    1. Static 파일들을 담을 폴더 만들기.
        - APP폴더 안에 Static폴더 만들기
    2. Static 파일이 어디 있고, 어디로 모을지 알려주기
        - setting.py에서 알려주기 
    3. Static파일 한 곳에 모으기
        - $ python manage.py collectstatic 명령어 사용하기
    4. 1~3번 완료 후 html상에 static파일을 사용한다고 알려준 후 static파일 사용
