from django.shortcuts import render
from django.http import HttpResponse
import qrcode
import time
# Create your views here.


def home(request):
    res = render(request,'code_scanner/home.html')
    return res


def search(request):
    if request.method=='POST':
        text = request.POST['text']
        url = qrcode.make(text)
        print(text)
        url.save('E:\Django_new\project_code_scanner\code_scanner\static\code_scanner\images\code.png', scale=6)
        time.sleep(5)
        print("here is the type: ",type(url))
        flag=1
        res = render(request,'code_scanner/home.html',{'text':text,'flag':flag,'url':url})
        return res

