from django.shortcuts import render

# Create your views here.

def index(request):

    print 'change by cdb'

    return render(request,'index.html',locals())