from django.http import HttpResponse
def index(request):
    HttpResponse('<h1>首页</h1>')
    pass
