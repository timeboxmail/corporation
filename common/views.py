from django.shortcuts import render

# Create your views here.

def index(request):
    print 'ggggggggg'
    return render(request,'index.html',locals())