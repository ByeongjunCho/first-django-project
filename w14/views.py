from django.shortcuts import render

# Create your views here.

def push(request):
    # 사용자에게 form을 전송한다.
    return render(request, 'w14/push.html')

def pull(request):
    # 사용자가 입력한 값을 받는다.
    print(request.GET)
    number = request.GET.get('number')
    context = {
        'number': number
    }
    return render(request, 'w14/pull.html', context)    