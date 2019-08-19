# Django

## 1. 시작하기

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

### 0. 가상환경 실행 + .gitignore

> 가상환경을 사용하는 이유는 프로젝트마다 활용되는 라이브러리(pip)가 다르고, 동일한 라이브러리더라도 버전이 다를 수 있다. 
>
> 따라서, 프로젝트를 수행하면서 라이브러리 삭제 혹은 변경을 하는 것이 아니라 각 프로젝트마다 독립된 가상환경을 부여하여 의존성을 없앤다.
>
> 항상 django를 실행할 때마다 가상환경을 활성화 시키는 것을 습관화 하자!
>
> 추후 Data Science/Deep Learning 학습은 anaconda를 활용하기도 한다.

가상환경은 python에서 기본으로 제공하고 있는 `venv`를 활용한다.

1. 가상환경 생성

   원하는 디렉터리에서 아래의 명령어를 입력한다,.

   ```bash
   $ python -m venv __venv__
   ```

   * `__venv__` 여기에 가상환경 이름을 작성하는데, 보통 `venv`라고 설정한다.
   * `__venv__`폴더가 생성되는데, 구조는 다음과 같다.
     * `Lib`: 가상환경에 설치된 라이브러리 모음.
     * `Scripts`: 가상환경 실행과 관련된 파일

2. 가상환경 실행

   ```bash
   $ ls
   venv/ ....
   $ source venv/Scripts/activate
   $ python -V
   Python 3.7.4
   ```

   * 반드시 해당 명령어는 `venv`폴더가 있는 곳에서 실행시킨다.
   * **`bash shell`에서는 `activate`파일을 실행하여야 한다.**
     * `cmd`: `activate.bat`
     * `power shell`: `activate.ps1`

3. 가상환경 종료

   ```bash
   $ deactivate
   ```

4. `.gitignore`등록

   ```
   venv/
   ```

   * 추가적으로 visual studio code를 활용하는 경우에는 `.vscode/`
   * python 환경에서는 `__pycache__/`
   * pycharm 환경에서는 `.idea/`

   위의 폴더들은 `.gitignore`에 등록하는 습관을 가지자! 잘 모르겠으면 [gitignore.io](gitignore.io)에서 찾아서 복사하자



### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```

```bash
$ django-admin startproject __프로젝트이름__ .
```

* 프로젝트 이름으로 구성된 폴더와 `manage.py`가 생성된다.
  * `__init__.py`: 해당 폴더가 패키지로 인식될 수 있도록 작성되는 파일
  * `setting.py`: **django 설정과 관련된 파일**
  * `urls.py`: **url 관리**
  * `wsgi.py`: 배포시 사용(web server gateway interface). 파이썬에서 사용되는 웹 서버
  * `manage.py`: **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티**

### 2. 서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000`으로 들어가서 로켓 확인!

### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

* `app이름`인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py`: 관리자 페이지 설정

  * `apps.py`: app의 정보 설정. 직접 수정하는 경우 별로 없음.

  * `models.py`: **MTV-Model을 정의하는 곳**

  * `tests.py`: 테스트 코드를 작성하는 곳.

  * `views.py`: **MTV-View를 정의하는 곳.**

    * 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html)
      ```

**app을 만들과 나서 반드시 `settings.py`에서 `INSTALLED_APPS`에 app을 등록한다.**

```python
# first_django.setting.py
# ..
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    ...
]
# ..
```

## 2. 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index),
]
```

* `urls.py`는 우리의 웹 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
* path(`경로`, `views에 정의된 함수`)

### 2. View 정의

```python
# pages/views.py

def index(requests):
    return render(request, 'index.html')
```

* `views.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.

### 3. Template 정의

* 기본적으로 `app`을 생성하면, `templates`폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    안녕 장고야
</h1>
```

### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000`에서 확인



## 3. 예제

```python
# urls.py 
# ....
from django.contrib import admin
from django.urls import path

# 1. url 설정
# pages app의 views.py 파일 불러오기
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. url 설정
    # path(url, 해당하는 views의 함수)
    path('', views.index),
    # variable routing
    # url의 특정 값을 변수처럼 활용
    path('hello/<str:name>/', views.hello),  
    path('lotto/', views.lotto),  
    path('dinner/', views.dinner), 
    path('cube/<int:num>/', views.cube),
    path('about/<str:name>/<int:age>/', views.about) # 주소에 입력되는 값을 받는 방법
]
```

```python
# app 이름__ views.py
import random
import datetime
from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의

def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

def hello(request, name):
    context = {'name':name}
    return render(request, 'hello.html', context)

def lotto(request):
    print(request)  # 요청 정보가 들어온다.
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 값을 딕셔너리에 담아서(보통 context라고 부름)
    context = {'numbers': numbers}
    # render 할때 3번째 인자로 넘겨준다
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨 준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)이다.
    return render(request, 'lotto.html', context)

def dinner(request):
    menus = ['롯데리아', '편의점도시락', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick, 
        'menus': menus, 
        'users': [],
        'sentence': 'Life is short, You need Python + django!',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google.com'
    }
    return render(request, 'dinner.html', context)

def cube(request, num):
    context = {
        'num': num,
        '3num': num**3,
        'numbers': [1,2,3],
        'students': {'a': 'a', 'b': 'b'}
        }
    return render(request, 'cube.html', context)

def about(request, name, age):  # urls에 정의한 주소값의 변수명과 같은 변수명을 사용해야 한다.
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'about.html', context)
```

다음과 같이 html + Django에서 사용 가능한 html 특수언어가 존재한다.

```html
<!--....... -->
<body>
  <!-- 1. 출력 -->
  <h1>오늘 저녁은 {{pick}}먹어!</h1>
  <h2>1. 반복문</h2>
  {% for menu in menus %}
  <li>{{menu}}</li>
  {% endfor %}
  <hr>
  {% for menu in menus %}
  <p>{{ forloop.counter }}: {{menu}}</p>
  {% endfor %}
  <hr>
  {% for user in users %}
  <p>{{user}}</p>
  {% empty %}
  <p>현재 가입한 유저가 없습니다!!</p>
  {% endfor %}
  <!-- 조건문 -->
  <h2>2. 조건문</h2>
  {% for menu in menus %}
    {% if menu == '치킨' %}
      <p>치킨은 푸라닭이지!!!</p>
    {% endif %}
  {% endfor %}
  <!-- lorem -->
  <h2>3. lorem</h2>
  <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eius impedit consequatur commodi, saepe id enim veniam earum, eaque dolor a, architecto ipsam! Officiis natus voluptatum dolore suscipit praesentium impedit obcaecati.</p>
  <p>{% lorem %}</p>
  <!-- lorem 갯수 w/p
  w : word
  p : paragraph
  -->
  <p>{% lorem 3 w %}</p>
  <p>{% lorem 1 p %}</p>
  <p>{% lorem 2 w random %}</p>
  <h2>4. 글자 관련 필터</h2>
  <p>{{ sentence|truncatewords:3}}</p>
  <p>{{sentence|truncatechars:10}}</p>
  <p>{{ sentence|length }}</p>
  <p>{{ sentence|lower }}</p>
  <p>{{ sentence|title }}</p>
  <p>{{ menus|random }}</p>
  <h2>5. 날짜 표현</h2>
  <p>{{ datetime_now }}</p>
  <p>{% now 'DATE_FORMAT' %}</p>
  <p>{% now 'DATETIME_FORMAT' %}</p>
  <p>{% now 'SHORT_DATETIME_FORMAT' %}</p>
  <p>{% now 'Y년 m월!' %}</p>
  <p>{{ datetime_now|date:'SHORT_DATE_FORMAT' }}</p>
  <p>{{ google_link|urlize }}</p>
```

