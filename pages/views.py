from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의

def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')